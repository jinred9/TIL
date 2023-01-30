> VS cod에서 ! -> enter key를 누르면 html head가 자동으로 생성된다.
# 1. HTML 시작하기
## 1.1 HTML 기본구조
### 1.1.1 HTML 기본구조 살펴보기
   ![HTML 기본구조1](./image/1.1%20HTML%20%EA%B8%B0%EB%B3%B8%EA%B5%AC%EC%A1%B01.bmp)
   ![HTML 기본구조2](./image/1.2%20HTML%20%EA%B8%B0%EB%B3%B8%EA%B5%AC%EC%A1%B02.bmp)
1. `<!DOCTYPE html>` : 현재 문서가 HTML5 언어로 작성한 웹 문서라는 뜻이다.
2. `<html> ~ </html>` : 웹문서의 시작과 끝을 나타내는 태그입니다. 웹 브라우저가 `<html>` 태그를 만나면 `</html>`까지 소스를 읽어 화면에 표시합니다.
3. `<head> ~ </head>` : 웹 브라우저가 웹 문서를 해석하는 데 필요한 정보를 입력하는 부분입니다.
4. `<body> ~ </body>` :실제로 웹브라우저 화면에 나타나는 내용입니다. 앞으로 우리가 공부할 HTML 태그는 대부분 `<body>`태그 안에 들어 있습니다.

### 1.1.2 웹 문서 구조를 만드는 시맨틱 태그
   시맨틱 태그는 웹문서 내용에 영향을 주지 않으면서 웹브라우저가 문서 구조를 파악하는데 중요한 역할을 하는 태그입니다.
   header, main, footer, nav, article, section, aside 태그로 해당 영역을 정의할 수 있다.

## 1.2 WEB 문서에 내용 입력하기
### 1.2.1 텍스트 태그들
   1. `<hn>` : 웹문서에서 제목을 표현하는 태그로 이다. `<h1> ~ <h6>`까지 크기를 조절하여 사용한다. `<h1>`이 가장크며, `<h6>`으로 갈수록 크기가 작아진다.
   2. `<p>` : 텍스트 단락을 입력할 때 사용한다.
   3. `<br>` : 줄 바꾸는 태그.
   4. `<blockquote>` : 인용문에 적용하는 태그로 들여쓰기를 표현할 때 사용한다.
   5. `<strong>`, `<b>` : 텍스트를 굵게 표시한다.
   6. `<em>`, `<i>` : 텍스트를 기울여 표시한다.
   7. `<abbr>` : 줄임말을 표시하고 title 속성을 함께 사용할 수 있다.
   8. `<cite>` : 웹문서나 포스트에서참고 내용을 표시한다.
   9. `<code>` : 컴퓨터 인식을 위한 소스코드이다.
   10. `<small>` : 부가 정보처럼 작게 표시해도 되는 텍스트입니다.
   11. `<sub>` : 아래 첨자를 표시한다.
   12. `<sup>` : 위 첨자를 표시한다.
   13. `<s>` : 취소선을 표시한다.
   14. `<u>` : 밑줄을 표시한다.
   15. `<ins>` : 공동 작업 문서에서 새로운 내용을 삽입합니다.
   16. `<del>` : 공동 작업 문서에서 기존 내용을 삭제합니다.
   * 예제
     * h6 : 영화<h6>영화</h6>
     * p : 영화<p>영화</p>
     * br : 영화<br>영화
     * blockquote : 영화<blockquote>영화</blockquote>
     * strong : 영화<strong>영화</strong>
     * b : 영화<b>영화</b>
     * em : 영화<em>영화</em>
     * i : 영화<i>영화</i>
     * abbr : 영화<abbr title="">영화</abbr>
     * cite : 영화<cite>영화</cite>
     * code : 영화<code>영화</code>
     * small : 영화<small>영화</small>
     * sub : 영화<sub>영화</sub>
     * sup : 영화<sup>영화</sup>
     * s : 영화<s>영화</s>
     * u : 영화<u>영화</u>
     * ins : 영화<ins>영화</ins>
     * del : 영화<del>영화</del>

### 1.2.2 목록 만들기
   1. 순서 있는 목록을 만드는 `<ol>`, `<li>`
      ol : ordered list
      li : list
      `<ol>`태그는 **type, start**속성을 가진다.
      type = "1", "a", "A", "i", "I"로 설정할 수 있다.
      순서목록은 '1'부터 시작하지만 start 속성을 사용하면 목록번호을 바꿀수도 있다.
      <ol type="I" start ="3">
         <li>빨강</li>
         <li>노랑</li>
      </ol>
   2. 순서 없는 목록을 만드는  `<ul>`, `<li>` 태그
      ul : unordered list
      순서 없는 목록은 목록들 앞에 작은 원이나, 사각형으로 리스트가 표현된다.
      <ul>
         <li>빨강</li>
         <li>노랑</li>
      </ul>
   3. 설명 목록을 만드는 `<dl>`, `<dt>`, `<dd>` 태그
      dl : description list
      설명 목록은 이름(name)과 값(value) 형태로 된 목록을 말합니다. 마치 사전에서 단어명과 설명이라고 볼 수 있다.
      <dl>
         <dt>선물용 3kg</dt>
         <dd>소과 13~16과</dd>
         <dd>중과 10~12과</dd>
      </dl>
### 1.2.3 표만들기
> 표에 사용되는 tag들은 `<table>`, `<caption>`, `<tr>`, `<td> 또는 <th>`, `<thead>`, `<tbody>`, `<tfoot>`가 있다.
> `<td>` 대신에 `<th>`를 사용할 수도 있다. `<th>`를 사용하면 내용이 진하게 표시되고 중앙배열되어 눈에 뛴다.
> rowspan : 열방향으로 cell을 합칠때 사용
> colspan : 행방향으로 cell을 합칠때 사용
> 열에 배경색을 넣는 등 style을 적용할 때 `<col>`, `<colgroup>`을 사용한다. `<col>`이 단독으로 사용할 때는 `<col>`만 쓰지만 2개 이상의 `<col>`을 적용할 때 `<colgroup>`을 사용한다.
```html
<table>
   <caption>표 제목</caption>
   <colgroup>
      <col style='background-color:#eee;'>
      <col>
      <col span='2' style='width:150px; background-color:#eee;'>
   </colgroup>
   <tr>
      <td>1행 1열</td> // td
      <th>1행 2열</th> // th
      <td>1행 3열</td>
      <td rowspan='2'>4열</td>
   </tr>
   <tr>
      <td>2행 1열</td>
      <td colspan='2'>2행 2열</td>
   </tr>
</table>
```
<table>
   <caption>표 제목</caption>
   <colgroup>
      <col style='background-color:#eee;'>
      <col>
      <col span='2' style='width:150px; background-color:#eee;'>
   </colgroup>
   <tr>
      <td>1행 1열</td>
      <th>1행 2열</th>
      <td>1행 3열</td>
      <td rowspan='2'>4열</td>
   </tr>
   <tr>
      <td>2행 1열</td>
      <td colspan='2'>2행 2열</td>
   </tr>
</table>

### 1.2.4 이미지 삽입
> **기본형** `<img src="이미지 파일경로 alt="대체용 텍스트">`
> 이미지 파일의 크기는 width, height속성으로 조절 가능하며, 2개모두 사용할 수도 있고, 1개만 적용하면 나머지 속성은 비율에 맞게 자동으로 적용되기도 한다. `%`와 `px`2개단위 모두 사용 가능하다.
```html
<img src='/image/1.2.4 image.jpg' alt='가방' width='100px'>
```
<img src='/image/1.2.4 image.jpg' alt='가방' width='100px'>

### 1.2.5 오디오와 비디오 삽입
1. object
**기본형** `<object width='너비' height='높이' data='파일'></object>`
`<object>`태그는 다양한 멀티미디어 파일을 삽입할 때 사용한다. **width**와 **height** 속성을 사용하여 삽입되는 미디어의 크기를 조절할 수 있다.
2. embed
**기본형** `<embed src='파일경로' width='너비' height='높이'>`
`<embed>`태그는 HTML 초기버젼부터 사용해서 대부분의 브라우저에서 사용가능하다. 닫는 태그가 없다. `<object>`, `<video>`, `<object>`를 지원하지 않는 웹 브라우저를 고려해야 한다면 `<embed>` 태그를 사용할 수 있다.
```html
<object width='300' height='400' data='/media/product.pdf'></object><br>
<embed width='300' height='400' src='/media/product.pdf'>
```
3. audio, video
**기본형** `<audio src='오디오 파일 경로'></audio>`
**기본형** `<video src='오디오 파일 경로'></video>`
* 속성
  * controls : 플레이어 화면에 컨트롤 바를 표시합니다.
  * autoplay : 자동으로 실행합니다.
  * loop : 반복 재생합니다.
  * muted : 소리를 제거합니다.
  * preload : 페이지를 불러올 때 오디오나 비디오 파일을 어떻게 로딩할 것인지 지정합니다. 사용할 수 있는 값은 auto, metadata, none입니다. 기본값은 preload='auto'입니다.
  * width, height : 두개 모두 지정가능하면, 한개만 지정할 경우 비율에 맞게 자동으로 계산해서 표시합니다.
  * poster='파일 이름' : `<video>`에서만 사용되는 속성으로 비디오가 재생하기 전에 화면에 표시될 포스터 이미지르 ㄹ지정합니다.

### 1.2.6 하이퍼링크 삽입
> 링크는 `<a>`태그를 쓰며, 링크할 주소나 파일은 **href**속성을 사용합니다.
> **기본형** `<a href='링크할 주소'>테스트 또는 이미지</a>`
> **target='_blank'**는 새탭에서 링크를 열어준다.
```html
<div>
   <p><a href='../05/order.html' target='_blank'>주문서작성</a></p>
</div>
```






