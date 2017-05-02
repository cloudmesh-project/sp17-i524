cm reset
# If cloudmesh is already installed
sudo pip uninstall cloudmesh_client

sudo pip install cloudmesh_client

cm refresh on
cm register profile
cm default cloud=chameleon #In case of a different default cloud it will change
cm default user=<USERNAME_REMOVED>
cm key add --ssh
cm key upload # Sometimes will throw an error if key is already present
cm secgroup upload

#The actual Hadoop deploymen starts now
cm cluster define --count 3 --image CC-Ubuntu14.04 --flavor m1.small
cm hadoop define spark pig
cm hadoop sync
cm hadoop deploy

