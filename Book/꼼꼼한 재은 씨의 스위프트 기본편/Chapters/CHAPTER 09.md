# CHAPTER 09 – 네트워크 통신과 API

# 9.1 네트워크 통신의 종류

- 앱과 서버 간 네트워크 통신이 이루어지는 방식은 크게 두 가지
    - TCP/UDP를 사용하는 소켓 방식의 연결성 통신
    - HTTP, HTTPS, SMTP 등의 프로토콜을 이용한 비연결성 통신

## 9.1.1 소켓 방식의 연결 지향 통신

- 소켓(Socket)을 이용한 네트워크 통신 방식은 보통 저수준(Low-level) 통신을 통하여 구현됨
    - TCP 연결 : 데이터 유실을 방지하고 완전한 전송을 보장하지만 상대적으로 덜 빠름
    - UDP 연결 : 데이터의 완전한 전송을 보장하지 않지만 상대적으로 더 빠름

## 9.1.2 비연결 지향 통신

- HTTP 등의 프로토콜을 사용하여 메시지를 주고받는 방식. 대표적으로 HTTP/HTTPS 프로토콜이 있음
- 비연결성 프로토콜은 요청이 들어오면 이에 맞는 응답을 보낸 후 바로 연결을 종료
- 비연결 방식이라 연결을 아예 하지 않는다는 뜻은 아니고 단지 연결을 유지하지 않는 것일 뿐이다.
- 필요 없는 네트워크 대역 소모를 줄일 수 있고, 서버 부하도 낮출 수 있어서 범용적인 모바일 서비스에 많이 사용됨
- 동일한 HTTP/HTTPS 프로토콜을 사용하지만 일반 HTML을 제공하는 웹 페이지(Web Page)와 달리, 데이터만을 주고받을 수 있도록 설계된 모듈을 웹 서비스(Web Service)라고 부름
- SOAP(Simple Object Access Protocol)은 일반적으로 널리 알려진 HTTP, HTTPS, SMTP 등의 프로토콜을 통해 양쪽에서 XML 형태의 메시지를 주고받도록 구현된 프로토콜이다. SOAP는 웹 서비스에서 메시지를 전달할 때 몇 가지 형태의 메시지 패턴 중에서 원격 프로시저 호출(Remote Procedure Call : RPC)이라고 불리는 클라이언트-서버 구조의 메시지 패턴을 많이 사용하며, 이때 통신 구조는 Envelope/Header/Body의 세 가지 영역으로 구분됨
- RESTful의 근간이 되는 REST(Representational State Transfer)는 월드 와이드 웹(World Wide Web. WWW)과 같은 분산 하이퍼 미디어 시스템을 위한 소프트웨어 아키텍처의 한 형식임. REST란 웹 형식을 빌어 데이터를 전송하되, SOAP나 쿠키 등 별도의 전송 프로토콜 없이 전송하기 위해 만들어진 간단한 형식의 인터페이스를 말함.
- REST 원리를 따라 구현된 시스템을 우리는 RESTful이라는 용어로 지칭함
- CRUD : 쓰기(Create), 읽기(Read), 수정(Update), 삭제(Delete)
- URI 구성 권고에 따르면 RESTful API 구성을 위한 URI에는 정보의 분류 체계만 포함되어야지, 정보를 어떻게 다룰 것인가 하는 동작에 관한 명세는 포함되지 않는 것이 좋음
- URI에 CRUD 동작을 포함하는 대신, URI 헤더에 이들 메소드를 사용하여 동작을 정의하는 것으로 RESTful API 동일한 URI라 하더라도 처리할 액션을 구분할 수 있음
- XML : Extensible Markup Language
- XML 형식의 마크업으로 전달된 데이터는 그대로 사용할 수 있는 것이 아니라 데이터를 형식에 맞게 분석하는 과정이 필요하다. 이 과정을 파싱(Parsing)이라고 하고, 파싱을 처리하는 모듈을 파서(Parser)라고 함. iOS에서는 파운데이션 프레임워크를 통하여 XMLParser 모듈을 제공함
- JSON : JavaScript Object Notation
- 집합 구조를 ‘JSON 객체’라고 부르며 정의할 때 중괄호를 사용하는 반면, 리스트 구조는 ‘JSON 배열’이라고 부르며 정의할 때 대괄호를 사용함
- JSON 객체는 { 키 : 데이터 } 형태로 이루어진 사전(Dictionary)식 데이터 집합이다.
- 따옴표를 붙여주는 처리를 쿼우팅(Quoting)이라고 함. 큰따옴표를 붙여주는 것을 더블 쿼우팅, 작은따옴표를 붙여주는 것을 싱글 쿼우팅이라고 한다.
- 네트워크를 통해 전달되는 JSON 대부분은 정렬되지 않은 형태로 전달됨
- 각각의 언어가 지원하는 자료형에 JSON 데이터를 저장하면 단순히 JSON 데이터 자체가 아니라 각 언어에서 제공하는 자료형으로 변환하여 사용할 수 있음
- 스위프트에서 딕셔너리는 동일한 타입의 데이터만 저장할 수 있다는 제약이 있다.
- NSDictionary는 한 번 데이터가 정의되고 나면 새로운 데이터를 추가하거나 수정/삭제할 수 없는 반면 NSMutableDictionary는 저장된 데이터를 얼마든지 수정/삭제할 수 있는 차이가 있다. 일반적으로 Mutable 키워드가 붙은 자료형이 함께 제공될 때, 이 키워드가 붙은 쪽은 편집이 가능하지만 붙지 않은 쪽은 편집이 불가능하다는 차이가 있다. 그 외 나머지 기능은 모두 동일하고 이들 자료형은 스위프트 언어에서 제공하는 것이 아니라 파운데이션 프레임워크를 통해 제공된다.

## 9.3.1 API 기본 정보

- JSON 배열 내부에 들어가는 항목을 ‘아이템’이라고 표현함
- 앱에서 <더 보기> 버튼을 통해 추가 데이터를 요청하는 방식을 페이징(Paging) 처리라고 함. 데이터에 대한 페이징 처리를 하려면 총 데이터 개수가 몇 개여야 하는지 알아야 하므로 이를 지원하기 위해 총 데이터 개수값을 제공하는 것이다.

## 9.3.2 네트워크 객체를 통한 데이터 요청 기능 구현

- REST 방식의 구현은 일반 웹 페이지를 호출할 때와 거의 동일한 코드로 구현이 가능하므로 단순히 웹 페이지를 호출하는 코드를 작성한다고 생각하면 구현하기 쉬움
- Data는 파운데이션 프레임워크에서 제공하는 클래스이다. 다양한 종류의 데이터를 변환 과정 없이 저장하기 위해 사용하는 이 객체는 텍스트 기반의 데이터뿐만 아니라 이미지나 동영상과 같은 바이너리 데이터도 담을 수 있어 여러 가지 종류의 데이터를 처리하는 데에 탁월한 효율성을 자랑한다.
- Data 객체는 NSData 객체가 가지고 있는 기능 대부분을 지원하고 서로 타입 캐스팅도 가능함
- Data 객체에서 제공되는 Data(contentsOf:) 초기화 구문은 복잡한 과정 없이도 손쉽게 GET 방식으로 RESTful 서비스를 호출하고 응답을 받아올 수 있도록 지원함
- Data(contentsOf:)를 통해 생성되는 인스턴스는 항상 옵셔널 타입
- REST API 호출은 Data(contentsOf:)이 담당
- URL 클래스는 문자열 형태의 네트워크 주소를 인자값으로 입력받아 파운데이션 프레임워크에서 사용하는 형식의 주소 객체를 생성한다
- 파운데이션 프레임워크에서 제공하는 NSString 객체는 입력받은 Data 객체를 문자열로 변환해주는 메소드를 지원하지만, 스위프트의 기본 자료형인 String은 이와 같은 직접적인 변환 메소드가 없어서 상대적으로 복잡한 과정을 거쳐 Data 객체를 변환한다.
- iOS 9부터 외부 네트워크 관련된 보안 규칙이 신설되었다. App Transport Security, 줄여서 ATS라고 부르는 규칙임. 네트워크 객체를 사용해서 SSL 보안 프로토콜을 사용하지 않는 네트워크에 접속하려면 plist 파일에서 특정 설정을 추가해야됨. SSL 보안 프로토콜은 서버와 클라이언트 사이의 통신에 대한 보안 체계로, 이 프로토콜을 적용하면 서버와 클라이언트 사이의 패킷은 모두 암호화되어 전송된다.
- SSL 보안 프로토콜이 적용된 네트워크는 접속시 https://를 사용하고 이를 적용하지 않은 일반 프로토콜은 http://를 사용함

## 9.3.3 전달받은 데이터를 파싱하여 화면에 출력

- NSDictionary는 키-값으로 된 데이터 구조를 저장하므로 JSONObject 포맷의 데이터와 호환됨. 만약 데이터가 리스트 형태로 전달되었다면 JSONArray 포맷과 호환되는 NSArray 객체를 사용해야 함
- 데이터를 파싱할 때는 파운데이션 프레임워크에서 제공하는 JSONSerialization 객체의 jsonObject() 메소드를 사용하는 것이 좋음.
- jsonObject() 메소드는 파싱 과정에서 오류가 발생하면 이를 예외로 던지도록 설계됨. 그래서 이 메소드를 사용하기 위해서는 do ~ try ~ catch 구문으로 감싸줘야함. 진행 도중에 오류가 발생하면 진행하던 과정을 멈추고 catch 블록 쪽으로 오류와 함께 실행 흐름이 전달됨
- as!는 옵셔널 타입의 객체를 캐스팅할 때 강제로 해제하여 캐스팅하라는 의미이고 해제하지 않고 옵셔널 타입을 유지한 채 하려면 as?를 사용하면 됨
- 루프 구문을 이용한 순회 처리는 영어로 Iterator라고 함
- NSString은 doubleValue 속성을 사용하여 내부적으로 Double 형태의 값으로 변환할 수 있음

## 9.3.4 더보기 기능 구현

- 대체로 서버 측에서 제공하는 데이터를 데이터를 데이터베이스의 테이블에 나누어 저장하는데, 전체 데이터를 한꺼번에 제공하려면 관련된 테이블들 전체의 데이터를 읽어와야 함. 이를 풀 스캔(Full-Scan)이라고 함. 저장된 데이터의 양이 많으면 서버의 처리 속도가 늦어지고 성능상의 문제를 일으킬 수 있음
- 정보 이용에는 파레토의 법칙(Pareto’s rules)이 적용되므로 상위 20%의 데이터가 전체 사용 비율의 80%를 차지함. 사용 빈도가 낮은 80%의 데이터를 메모리에 저장하는 것은 메모리 사용의 효울성에 대한 심각한 문제임
- 일단 화면 구현이 끝나면 테이블 뷰는 데이터 소스를 다시 읽어 들이지 않음. tableView(_:numberOfRowsInSection:)를 다시 호출하지 않음. 따라서 화면 구현이 완료된 후에 데이터가 추가되더라도 테이블 뷰는 기존에 있던 데이터 크기를 유지하게 됨. 이것을 갱신해서 데이터를 다시 읽어 들이도록 해야 함.
