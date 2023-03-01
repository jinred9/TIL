# 4) Git 기조

## [1] Git 초기 설정

> 최초 한번만 설정합니다. 매번 Git을 사용할 때마다 설정할 필요가 없습니다.

1. 누가 commit 기록을 남겼는지 확인할 수 있도록 이름과 이메일 설정합니다.
   작성자를 수정하고 싶을 때에는 이름, 메일 주소만 다르게 하여 동일하게 입력합니다.
```Bash
$ git config --global user.name "이름"
$ git config --global user.email "메일 주소"
```

2. 작성자가 올바르게 설정되었는지 확인 가능합니다.
```bash
$ git config --global -l
# 또는
$ git config --global --list
```
### (0) 로컬 저장소
![로컬저장소](/md_image/4-1%20Git%20local%20storage.png)
* `Wording Directory (= Working Tree)` : 사용자의 일반적인 작업이 일어난 곳
* `Staging Area(= Index)` : Commit을 위한 파일 및 폴더가 추가되는 곳
* `Repository` : staging area에 있던 파일 및 폴더의 변경사항(commit)을 저장하는 곳
* Git은 Working Directory -> Staging Area -> Repository 의 과정으로 버젼 관리를 수행합니다.

### (1) git init
```bash
$ git init
Initialized empty Git Repository in C:/uvers/kyle/git-prcatice/.git/

kyle@KYLE mingw64 ~/git-practice (master)
```
* 현재 작업 중인 디렉토리를 Git으로 관리한다는 명령어
* `.git`이라는 숨김폴더를 생성하고, 터미널에는 `(master)`라고 표기됩니다.
* Mac OS의 경우 `(master)`가 표기되지 않는데, Terminal 업그레이드를 통해 표기할 수 있습니다.
```markdown
주의 사항
1. 이미 Git 저장소인 폴더 내에 또 다른 Git 저장소를 만들지 않습니다.(중첩금지)
즉, 터미널에 이미 (master)가 있다면, git init을 절대 입력하면 안됩니다.
2. 절대 폼 디렉토리에서 git init을 하지 않습니다. 터미널의 경로가 `~`인지 확인합니다.
```

### (2) git status
```bash
$ git status
On branch master

No commits yet

nothing to commit (create/copy files and use "git add" tgit o track)
```
* Working Directory와 Staging Area에 있는 파일의 현재 상태를 알려주는 명령어
* 어떤 작업을 시행하기 전에 수시로 Status를 확인하면 좋습니다.
* 상태
  1. `Untracked` : Git이 관리하지 않는 파일(한번도 Staging Area에 올라간 적 없는 파일)
  2. `Tracked` : Git이 관리하는 파일
   a. `Unmodified` : 최신 상태
   b. `Modified` : 수정되었지만 아직 Staging Area에는 반영하지 않은 상태
   c. `Staged` : Staging Area에 올라간 상태
![파일의 라이프사이클](/md_image/4-2%20%ED%8C%8C%EC%9D%BC%EC%9D%98%20%EB%9D%BC%EC%9D%B4%ED%94%84%EC%82%AC%EC%9D%B4%ED%81%B4.png)

### (3) git add
```bash
# 특정 파일
$ git add a.txt

# 특정 폴더
$ git add myfolder/

# 현재 디렉토리에 속한 파일/폴더 전부
$ git add .
```
* Working Directory에 있는 파일을 Staging Area로 올리는 명령어
* Git이 해당 파일을 추정(관리)할 수 있도록 만듭니다.
* `Untracked, Modified -> Staged`로 상태를 변경합니다.
* 예시
```bash
$ touch a.txt b.txt

$ git status
On branch master

No commits yet

Untracked files: # 트래킹 되고 있지 않는 파일 목록
  (use "git add <file>..." to include in what will be committed)
        a.txt
        b.txt

nothing added to commit but untracked files present (use "git add" to track)
```
```bash
# a.txt만 Staging Area에 올립니다.

$ git add a.txt
```
```bash
$ git status

On branch master

No commits yet

Changes to be committed: # 커밋 예정인 변경사항(Staging Area)
  (use "git rm --cached <file>..." to unstage)
        new file:   a.txt

Untracked files: # 트래킹 되고 있지 않은 파일
  (use "git add <file>..." to include in what will be committed)
        b.txt
```

### (4) git commit
```bash
$ git commit -m "first commit"
[master (root-commit) c02659f] first commit
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 a.txt
```
* Staging Area에 올라온 파일의 변경 사항을 하나의 버전(commit)으로 저장하는 명령어
* `commit 메세지`는 현재 변경 사항들을 잘 나타낼 수 있도록 `의미`있게 작성하는 것을 권장합니다.
* 각각의 commit은 `SHA-1`알고리증에 의해 반환된 고유의 해시 값을 ID로 가집니다.
* `(root-commit)`은 해당 커밋이 최초의 커밋일 때만 표시됩니다. 이후 커밋부터는 사라집니다.

### (5) git log
```bash
$ git log
commit 1870222981b4731d14ef91d401c68c0bbb2f6e7d (HEAD -> master)
Author: kyle <kyle123@hphk.kr>
Date:   Thu Dec 9 15:26:46 2021 +0900

    first commit
```
* 커밋의 내역(`ID, 작성자, 시간, 메세지 등`)을 조회할 수 있는 명령어
* 옵션
  * `--oneline` : 한 줄로 축약해서 보여줍니다.
  * `--graph` : 브랜치와 머지 내역을 그래프로 보여줍니다.
  * `--all` : 현재 브랜치를 포함한 모든 브랜치의 내역을 보여줍니다.
  * `--reverse` : 커밋 내역의 순서를 반대로 보여줍니다.(최신이 가장 아래)
  * `-p` : 파일의 변경 내용도 같이 보여줍니다.
  * `-2` : 원하는 갯수 만큼의 내역을 보여줍니다.(2말고 임의의 숫자 사용가능)


- 옵션과 인자
  명령어를 사용하면서 `-` 혹은 `--`를 통해 옵션을 사용하는 것을 배웠습니다.
  옵션과 더불어서 인자라는 개념도 존재하는데요. 옵션과 인자 무엇이 다를까요?
  **옵션**은 명령어의 동작 방식을 지정하는 것입니다. 따라서 **생략 가능**합니다.
  단순히 기존 기능보다 부가적인 기능을 원할 때 사용합니다.
  예를 들면 `git log --oneline`은 커밋내역을 한 줄로 보고 싶을 때 사용합니다.
  `oneline` 옵션은 말 그대로 부가적인 기능이므로, 생략해도 `git log`는 정상 동작합니다.
  **인자**는 명령어의 동작 대상을 지정하는 것입니다. 따라서 **생략이 불가능** 합니다.
  예를 들면 `git add`라고만 작성하면 어떤 파일을 Staging Area에 올릴지 모르게 됩니다.
  반드시 `git add a.txt`와 같이 git add 명령어가 동작할 대상을 지정해야 하는데 이때 `a.txt와 같은 대상을 인자라고 합니다.

### (6) 한눈에 보는 Git 명령어
![Git 명령어](/md_image/4-3%20Git%20%EB%AA%85%EB%A0%B9%EC%96%B4.png)

# 5) Github
## [1] 원격저장소
> 여태까지는 내 컴퓨터라는 한정된 공간에 있는 로컬 저장소에서만 버전 관리를 진행했습니다. 이제는 Github의 원격저장소를 이용해 내 컴퓨터의 로컬 저장소를 다른 사람과 `공유`해 봅시다. Git의 주요 목적 중 하나인 `협업`을 위해 로컬 저장소와 원격 저장소의 연동 방법을 학습합니다.
### (1) Github에서 원격저장소 연결
1. 원격 저장소의 HTTPS 주소를 복사합니다.
2. 내 컴퓨터의 홈 디렉토리의 연결할 폴더에서 VScode를 엽니다.
3. git init을 통해 해당 폴더를 로컬저장소로 만들어 줍니다.
```bash
kyle@KYLE MINGW64 ~/TIL
$ git init
Initialized empty Git repository in C:/Users/kyle/TIL/.git/
```
4. git remote
   로컬 저장소에 원격 저장소를 `등록, 조회, 삭제`할 수 있는 명령어
   1. 등록
      `git remote add <이름> <주소>` 형식으로 작성합니다.
      ```bash
      $ git remote add origin https://github.com/edukyle/TIL.git
      ```
      [풀이]
      git 명령어를 작성할건데, remote(원격 저장소)에 add(추가) 한다.
      origin이라는 이름으로 https://github.com/edukyle/TIL.git라는 주소의 원격 저장소를 연결한다.
   2. 조회
      `git remote -v`로 작성한다.
      ```bash
      $ git remote -v
      origin  https://github.com/edukyle/TIL.git (fetch)
      origin  https://github.com/edukyle/TIL.git (push)

      add를 이용해 추가했던 원격 저장소의 이름과 주소가 출력됩니다.
      ```
   3. 삭제
      `git remote rm <이름>` 혹은 `git remote remove <이름>`으로 작성합니다.
      > 로컬과 원격 저장소의 연결을 끊는 것이지, 원격 저장소 자체를 삭제하는 것이 아니다.
      ```bash
      $ git remote rm origin
      $ git remote remove origin
      ```
      [풀이]
      git 명령어를 작성할건데, remote(원격 저장소)와의 연결을 rm(remove, 삭제) 한다.
      그 원격 저장소의 이름은 origin이다.
### (2) 원격 저장소에 업로드
* **파일을 업로드하는 게 아니라 커밋을 업로드 하는 것입니다.**
* 따라서 먼저 로컬 저장소에서 커밋을 생성해야 원격저장소에 업로드 할 수 있습니다.
1. 로컬 저장소에서 커밋 생성
```bash
# 현재 상태 확인

$ git status
On branch master

No commits yet

Untracked files:
  (use "git add <file>..." to include in what will be committed)
        day1.md

nothing added to commit but untracked files present (use "git add" to track)
```
```bash
$ git add day1.md
```
```bash
$ git commit -m "Upload TIL Day1"
[master (root-commit) f3d6d42] Upload TIL Day1
 1 file changed, 0 insertions(+), 0 deletions(-)
 create mode 100644 day1.md
```
```bash
# 커밋 확인

$ git log --oneline
f3d6d42 (HEAD -> master) Upload TIL Day1
```

2. `git push`
* 로컬 저장소의 커밋을 원격 저장소에 업로드하는 명령어
* `git push <저장소이름> <브랜치 이름>` 형식으로 작성합니다.
* `-u`옵션을 사용하면, 두 번째 커밋부터는 `저장소 이름, 브랜치 이름`을 생략 가능합니다.
```bash
$ git push origin master
```
[풀이]
git 명령어를 사용할건데, origin이라는 이름의 원격 저장소의 master 브랜치에 push 한다.이후에는 $ git push 라고만 작성해도 push가 됩니다.

* 주의
   Github 원격 저장소에 절대로 파일을 드래그해서업로드 하지 않습니다.!!!
   가끔 Github를 구글 드라이브처럼 여겨서, 파일을 직접 드래그해서 올리는 경우가 있습니다. Git 명령어를 학습했기 때문에, 반드시 git add -> git commit -> git push의 단계로만 업로드 해야합니다.
   그 이유는 로컬 저장소와 원격 저장소의 동기화 때문입니다.
   로컬 저장소에서 변경이 먼저 일어나고, 그 변경 사항을 원격 저장소에 반영하는 형태여야 합니다. 하지만, Github에 드래그를 해서 업로드를 하면 원격 저장소에 변경이 먼저 일어나는 형태가되기 때문에 이러한 행동을 지양해야 합니다.

3. `git push`를 그림으로 이해하기
![git push](/md_image/5.%20git%20push.png)

# Github README profile
1. [github-readme-stats](https://github.com/anuraghazra/github-readme-stats)를 이용하여 readme 파일을 꾸밀수 있다.
2. Gibhub profile 예시
   1. https://github.com/pifafu
   2. https://github.com/katmeister
   3. https://github.com/jlengstorf
   4. https://github.com/simonw
   5. https://github.com/CyrisXD
   6. https://github.com/kautukkundan/Awesome-Profile-README-templates/blob/master/dynamic-realtime/quadrified.md
3. 유용한 도구
   1. https://shields.io/
   2. https://github.com/alexandresanlim/Badges4-README.md-Profile
   3. https://github.com/anuraghazra/github-readme-stats

# 6) Clone, pull
## [1] 원격 저장소 가져오기
### (1) git clone
* 원격 저장소의 커밋 내역을 모두 가져와서, 로컬 저장소를 생성하는 명령어
* clone은 `복제`라는 뜻으로, `git clone`명령어를 사용하면 원격 저장소를 통째로 복제해서 내 컴퓨터에 옮길 수 있다.
* `git clone <원격 저장소 주소>`의 형태로 작성한다.
```bash
$ git clone https://github.com/edukyle/TIL.git
Cloning into 'TIL'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Total 3 (delta 0), reused 3 (delta 0), pack-reused 0
Receiving objects: 100% (3/3), done.
```
  위에 작성한 대로 실행하면, `Github의 edukyle이라는 계정의 TIL 원격 저장소를 복제`하여 내 컴퓨터에 TIL이라는 이름의 로컬 저장소를 생성하게 됩니다.
* git clone을 통해 생성된 로컬 저장소는 `git init`과 `git remote add`가 이미 수행된 상태가 됩니다.

### (2) git pull
* 원격 저장소의 변경 사항을 가져와서, 로컬 저장소를 업데이트하는 명령어
* 로컬 저장소와 원격 저장소의 내용이 완전히 일치하면 git pull을 해도 변화가 일어나지 않습니다.
* `git pull <저장소 이름> <브랜치 이름>
```bash
$ git pull origin master
From https://github.com/edukyle/git-practice
 * branch            master     -> FETCH_HEAD
Updating 6570ecb..56809a9
Fast-forward
 README.md | 1 +
 1 file changed, 1 insertion(+)

[풀이]
git 명령어를 사용할건데, origin이라는 원격 저장소의 master 브랜치의 내용을 가져온다.
```
* git clone vs git pull
  `git clone`은 git init 처럼 처음에 한번만 실행합니다. 즉 로컬 저장소를 만드는 역할이다. 단, git init처럼 직접 로컬 저장소를 만드는게 아니라, Github에서 저장소를 복제해서 내 컴퓨터에 똑같은 복제본을 만든다는 차이가 있습니다.
  `git pull`은 git push처럼 로컬 저장소와 원격 저장소의 내용을 동기화하고 싶다면 언제든 사용합니다. 단, push는 로컬 저장소의 변경 내용을 원격 저장소에 반영하는 것이고, pull은 원격 저장소의 변경 내용을 로컬 저장소에 반영하는 것입니다.
  