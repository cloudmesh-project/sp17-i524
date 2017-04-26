db.getSiblingDB("admin").auth("user1", "user1_password" )
use mlb
var mapFunction1 = function() {
                       emit(this.strikeOrFoul, this.Speed);
                   };
var reduceFunction1 = function(keystrikeOrFoul, valuesSpeed) {
                          return Array.avg(valuesSpeed);
                      };
db.pitches.mapReduce(
                     mapFunction1,
                     reduceFunction1,
                     {  
			query: { Speed: { $gt: 0 } },
			out: "strike_speeds" 
		     }
                   )
db.strike_speeds.find()
