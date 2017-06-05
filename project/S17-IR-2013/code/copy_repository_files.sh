bak_var=`date +%H%M%S`
outbrain=$HOME/outbrain
if [ -d "$outbrain" ]; then
 mv $outbrain $HOME/$bak_var
fi;
mkdir $outbrain
find ~/classes/github/cloudmesh/sp17-i524/project/S17-IR-2013/code -type f -print0 | xargs -0 cp -t $outbrain
##mv --backup=t <source_file> <dest_file>
cd $HOME/outbrain
wget https://iu.box.com/s/3mb9aiegh6boswlbbe3yg14if8fcfkfq 
mv $outbrain/3mb9aiegh6boswlbbe3yg14if8fcfkfq $outbrain/dataset.tgz
