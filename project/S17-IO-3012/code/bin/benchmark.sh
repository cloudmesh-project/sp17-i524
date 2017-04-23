#!/usr/bin/env bash

cd ../work

if [ -z "$1" ]
  then
    echo "Benchmark size must be specified" >&2; exit 1
fi

ip_address=$(head -n 1 mongos_main_ip.txt)
user_name=$(head -n 1 clouduser.txt)
path=$(head -n 1 clouddir.txt)
size=$1

if  [ $size != "large" ] && [ $size != "small" ]
then
  echo "Benchmark size of large or small must be specified" >&2; exit 1
fi

if  [ $size == "large" ] 
then
  echo "Warning: large import may run for 15 minutes or more"
fi

echo "$(date +"%F--%k:%M:%S")...delete any data from prior tests"
#make sure there is no data in the table from prior test
ssh $user_name@$ip_address "mongo < $path/delete_collection.js" > ../work/delete.out

echo "$(date +"%F--%k:%M:%S")...starting mongoimport"
SECONDS=0
#ssh $user_name@$ip_address "mongoimport --quiet --authenticationDatabase admin --username user1 --password user1_password --db mlb --collection pitches --file $path/data/pitches.csv --type=CSV --fields pitchID,atbatID,gamePitchID,description,strikeOrFoul,ball,inPlay,x,y,Speed,type,Screwball,Ephuus,KnuckleCurve,Forkball,TwoSeamFastball,Splitter,Slider,FourSeamFastball,Sinker,ChangeUp,Fastball,Curve,Cutter,Knuckle,Unknown,Confidence,KZTop,KZBottom,HorizPlateCross,VertPlateCrosss,TheoreticalStrike,TheoreticalBall,hInside,hOutside,hMiddle,vHigh,vLow,vMiddle,Position,HorzMovement,VertMovement,DistanceBreakOccurs,BreakAngle,BreakLength,releasePointHorz,releasePointDistance,releasePointVert,releasePointVelocityHorz,releasePointVelocityDistance,releasePointVelocityVert,releasePointAccelerationHorz,releasePointAccelerationDistance,releasePointAccelerationVert,on1B,on2B,on3B,play_guid,pitchSequence,balls,strikes" > ../work/import.out
ssh $user_name@$ip_address "mongoimport --quiet --authenticationDatabase admin --username user1 --password user1_password --db mlb --collection pitches --file $path/data/pitches_$size.csv --type=CSV --fields pitchID,atbatID,gamePitchID,description,strikeOrFoul,ball,inPlay,x,y,Speed,type,Screwball,Ephuus,KnuckleCurve,Forkball,TwoSeamFastball,Splitter,Slider,FourSeamFastball,Sinker,ChangeUp,Fastball,Curve,Cutter,Knuckle,Unknown,Confidence,KZTop,KZBottom,HorizPlateCross,VertPlateCrosss,TheoreticalStrike,TheoreticalBall,hInside,hOutside,hMiddle,vHigh,vLow,vMiddle,Position,HorzMovement,VertMovement,DistanceBreakOccurs,BreakAngle,BreakLength,releasePointHorz,releasePointDistance,releasePointVert,releasePointVelocityHorz,releasePointVelocityDistance,releasePointVelocityVert,releasePointAccelerationHorz,releasePointAccelerationDistance,releasePointAccelerationVert,on1B,on2B,on3B,play_guid,pitchSequence,balls,strikes" > ../stdlist/import.log
import_time=$SECONDS

echo "$(date +"%F--%k:%M:%S")...starting find command"
SECONDS=0
ssh $user_name@$ip_address "mongo < $path/find_collection.js" > ../stdlist/find.log
find_time=$SECONDS

echo "$(date +"%F--%k:%M:%S")...starting MapReduce"
SECONDS=0
ssh $user_name@$ip_address "mongo < $path/mapreduce.js" > ../stdlist/mapreduce.log
mapreduce_time=$SECONDS

echo 'Performance Summary'
echo "mongoimport: $import_time seconds"
echo "find: $find_time seconds"
echo "mapreduce: $mapreduce_time seconds"

echo "test_size" > test_size.csv
echo "$size" >> test_size.csv
echo "import_time" > import_time.csv
echo "$import_time" >> import_time.csv
echo "find_time" > find_time.csv
echo "$find_time" >> find_time.csv
echo "mapreduce_time" > mapreduce_time.csv
echo "$mapreduce_time" >> mapreduce_time.csv

currentdate=$(date +"%Y%m%d%H%M")

paste -d, current_config.csv test_size.csv > benchmark0.csv
paste -d, benchmark0.csv import_time.csv > benchmark1.csv
paste -d, benchmark1.csv find_time.csv > benchmark2.csv
paste -d, benchmark2.csv mapreduce_time.csv > ../benchmark/benchmark_$currentdate.csv

