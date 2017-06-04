bak_var=`date +%H%M%S`
if [ -d "$HOME/outbrain" ]; then
 mv $HOME/outbrain $HOME/$bak_var
fi;
mkdir $HOME/outbrain
find ~/classes/github/cloudmesh/sp17-i524/project/S17-IR-2013/code -type f -print0 | xargs -0 cp -t ~/outbrain
##mv --backup=t <source_file> <dest_file>
