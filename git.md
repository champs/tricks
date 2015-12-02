# gittrick
==========


Another Git trick and trip.

***
***git rename branch*** - basicly create a new branch and delete the old one

```shell
	git branch -m <newbranch>  
	git push origin --set-upstream <newbranch>  
	git push origin :<oldbranch>  
```

***submodule for each*** - 


***Clean up Corrupted module*** -
```shell
From redmine.local:/onesrc/smashfs
 * branch            champ/test -> FETCH_HEAD
Updating 3f0c957..22e9c7b
error: object file .git/objects/1f/fb2775043b843503dd37ca52cd5787dc2bf06f is empty
error: object file .git/objects/1f/fb2775043b843503dd37ca52cd5787dc2bf06f is empty
fatal: loose object 1ffb2775043b843503dd37ca52cd5787dc2bf06f (stored in .git/objects/1f/fb2775043b843503dd37ca52cd5787dc2bf06f) is corrupt
```
```shell

	find .git/objects/ -size 0 -delete.
```
