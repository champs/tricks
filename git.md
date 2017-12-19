# gittrick
==========


Another Git trick and trip.

***
***git rename branch***
basicly create a new branch and delete the old one

```shell
	git branch -m <newbranch>  
	git push origin --set-upstream <newbranch>  
	git push origin :<oldbranch>  
```

***submodule for each***


***Clean up Corrupted module***
```shell
From gitserver.local://repo/test
 * branch            champ/test -> FETCH_HEAD
Updating 3f0c957..22e9c7b
error: object file .git/objects/1f/fb2775043b843503dd37ca52cd5787dc2bf06f is empty
error: object file .git/objects/1f/fb2775043b843503dd37ca52cd5787dc2bf06f is empty
fatal: loose object 1ffb2775043b843503dd37ca52cd5787dc2bf06f (stored in .git/objects/1f/fb2775043b843503dd37ca52cd5787dc2bf06f) is corrupt
```
```shell

	find .git/objects/ -size 0 -delete.
```


***Change email for all previous commit***
```
git filter-branch --env-filter '
OLD_EMAIL="OLD@EMAIL.com" 
CORRECT_NAME="Name LastName" 
CORRECT_EMAIL="NEW@EMAIL.com" 
if [ "$GIT_COMMITTER_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_COMMITTER_NAME="$CORRECT_NAME"
    export GIT_COMMITTER_EMAIL="$CORRECT_EMAIL"
fi
if [ "$GIT_AUTHOR_EMAIL" = "$OLD_EMAIL" ]
then
    export GIT_AUTHOR_NAME="$CORRECT_NAME"
    export GIT_AUTHOR_EMAIL="$CORRECT_EMAIL"
fi
' --tag-name-filter cat -- --branches --tags

```


***Git bundle***
Use git bundle to deploy a code to a remote server that can not to git server.

```shell
git bundle create filename.bundle -b <branch>
scp filename.bundle <server>:<path>
-- on remote server
> git clone -b <branch> filename.bundle <targetdir>
```

***Git config***
`git config --global push.default simple`


***Git upstream***
git remote add <remotename> <git clone url>
git fetch <remotename>
git checkout <remotename>/<branchname> -b <new localbranch>

