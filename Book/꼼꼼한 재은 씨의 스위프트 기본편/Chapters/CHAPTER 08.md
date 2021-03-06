# CHAPTER 08 – 테이블 뷰를 이용한 데이터 목록 구현

- 테이블 뷰 컨트롤러를 이용하여 수평적 관계의 카테고리나 콘텐츠를 병렬로 배열하고, 수직적 관계로 세분한 정보들을 내비게이션 컨트롤러를 통하여 직렬로 표현하여 전체적인 앱의 콘텐츠 표현 구조를 구성함
- 일반적으로 알려진 정보 검색 알고리즘에 따르면, 가장 효율적인 정보 접근 방법은 콘텐츠를 성격에 따라 계층으로 구조화하는 것
- 가장 고려해야 할 부분은 더 적은 횟수의 선택 과정으로 원하는 정보를 찾을 수 있게 하는 것
- 데이터베이스의 설계 원리에 ‘선택도(Cardinality)’라는 것이 있는데, 특정 카테고리를 선택하여 나온 결과값의 개수가 적을수록 ‘선택도가 높다’고 표현하며 콘텐츠 분류가 잘 되었다고 할 수 있음.

# 8.1 테이블 뷰 컨트롤러

- 섹션은 하나의 테이블 뷰 내에서 셀들을 그룹으로 묶을 수 있는 단위

# 8.2 프로토타입 셀

- 가독성과 코딩 규칙을 위해 권장되는 몇 가지 사항
    - 뷰 컨트롤러를 구현하는 커스텀 클래스면 가급적 이름 뒤에 **Controller 접미사를 붙여주는 것이 좋음
    - 파일의 이름과 클래스의 이름은 일치시켜주는 것이 좋음
    - 클래스 이름은 항상 대문자로 시작하되, 클래스의 역할과 성격을 분명하게 드러내는 이름으로 작성해 주어야 함
- 테이블 뷰 셀에서 Accessory 속성은 셀의 오른쪽 끝에 표시될 아이콘을 선택하는 데에 사용됨

# 8.3 데이터 소스

- 테이블 뷰의 각 행마다 대응할 수 있도록 배열 형태이기만 하면 데이터 소스가 된다. 이렇게 만들어진 데이터 소스를 테이블 뷰 각 행에 연결하는 과정을 데이터 바인딩(Data Binding)이라고 함

## 8.3.1 데이터 소스 만들기

- 데이터 저장을 전담하는 클래스를 별도로 분리하는 설계 방식을 Value Object 패턴이라고 부름. Value Object 패턴은 보통 데이터 저장을 위한 클래스임을 쉽게 식별할 수 있게 하려고 클래스의 마지막에 VO라는 접미사를 붙임
- 리팩토링(Refactoring)은 코드의 결과나 성능에는 영향을 미치지 않고 단지 가독성과 유지 보수의 편의를 위해 더 세련되고 구조화된 코드로 변경하는 것을 말함
- 데이터 세트를 구성할 때에는 가급적 프로그래밍 로직이 포함되지 않게 하는 것이 좋음
- lazy 키워드를 붙여서 변수를 정의하면 참조되는 시점에 맞추어 초기화되므로 메모리 낭비를 줄일 수 있다.
- lazy 키워드를 붙이지 않은 프로퍼티는 다른 프로퍼티를 참조할 수 없음

## 8.3.2 테이블 뷰와 데이터 소스 연동

- dequeueReusableCell(withIdentifier:) 메소드는 인자값으로 입력받은 아이디를 이용하여 스토리보드에 정의된 프로토타입 셀을 찾고, 이를 인스턴스로 생성하여 우리에게 제공함. 이 과정에 재사용 큐(Reusable Queue)라는 객체가 관여한다. 테이블 뷰 객체가 제공하는 재사용 큐는 한 차례 사용된 테이블 셀 인스턴스가 폐기되지 않고 재사용을 위해 대기하는 공간이다. 만약 위 메소드가 호출되었을 때 입력된 아이디에 맞는 인스턴스가 큐에 있다면 이 인스턴스를 꺼내어 재사용하고, 만약 입력된 아이디에 맞는 인스턴스가 큐에 없다면 새로 생성하여 제공하는 방식으로 동작함.
- 옵셔널 체인은 옵셔널로 선언된 객체를 사용할 때 매번 nil 여부를 체크해야 하는 비효율성을 줄이기 위한 문법으로, 옵셔널 타입의 객체와 그의 속성 사이에서 ? 연산자를 통해 구현됨. 이렇게 작성된 옵셔널 타입은 값이 있을 경우 작성된 내용을 정상적으로 실행하지만, 값이 비어 있더라도 실행을 건너뛸 뿐 오류를 발생시키지 않음
- 값이 비어있을 가능성이 있는 변수는 오류 방지와 간결한 처리를 위해 옵셔널 타입으로 처리하는 것이 스위프트의 특징이다.
- NSLog() 객체는 문자열로 입력된 값을 Xcode의 콘솔 로그 창에 출력해주는 기능을 함.
- 코드 스니펫 기능 : 자동 완성 기능 (esc 키를 누르기)

## 8.4.3 프로토타입 셀에 섬네일 이미지 추가하기

- UIImage(named: ) 방식으로 생성한 이미지 객체는 한 번 읽어온 이미지를 메모리에 저장해둔 다음, 두 번째 호출부터는 메모리에 저장된 이미지를 가져옴.
    - 이렇게 저장된 메모리는 이미지 객체를 다 사용한 후에도 잘 해제되지 않음.
    - 용량이 크고 한 번만 사용하는 이미지를 이 방식으로 읽어 들이면 메모리 관리에 빨간 불이 켜짐
- 이미지 객체로 인한 메모리 점유가 걱정되는 경우에는 UIImage(contentsOfFile: ) 생성자를 사용해서 이미지 객체를 생성하는 것이 좋음. 이 생성자를 사용하여 생성된 이미지 객체는 캐싱되지 않는 특징이 있음.
- 캐싱(Caching)은 데이터베이스나 파일 입출력 시스템 등에서 불러온 데이터를 메모리 등 고속으로 접근할 수 있는 곳에 임시로 저장해두고(이를 캐시라고 함), 이후 동일한 데이터를 읽어야 할 때 임시 저장소에서 데이터를 읽어오는 처리 방식을 말함.

## 8.5.1 tableView(_:estimatedHeightForRowAt:)

- tableView(_:estimatedHeightForRowAt:) 메소드가 구현되면 UITableView 객체의 rowHeight 속성은 더 이상 행의 높이값으로 역할을 하지 못 함.
- rowHeight 속성은 테이블 뷰의 모든 행 높이를 일괄로 제어하지만, tableView(_:estimatedHeightForRowAt:) 메소드는 각각의 행 높이를 다르게 제어해줄 수 있음.
- reloadData()는 테이블 뷰에 정의되어 있는 메소드로 데이터 소스를 다시 읽어와 목록을 갱신하는 역할을 함.
- ??는 Nil-Coalescing Operator라는 의미의 연산자이다.
    - A ?? B 구문은 “만약 A가 nil이 아닐 경우 옵셔널을 해제하고, nil일 경우 대신 B 값을 사용하라”
    - 우리말로 번역하면 Nil 병합 연산자
    - 이 연산자를 사용하면 옵셔널 타입이 해제됨
    - 이 연산자의 앞쪽에는 옵셔널 값이, 뒤쪽에는 일반값이 위치
    - 이 연산자의 뒤쪽에 위치한 일반 값의 타입은 앞쪽 옵셔널 값에서 옵셔널을 해제한 타입과 일치해야 한다.
- 셀프 사이징 셀(Self-Sizing Cell)은 콘텐츠에 따라 자동으로 높이가 조절됨
- estimatedRowHeight 프로퍼티는 셀 전체의 높이를 결정하기 전에 임시로 사용할 셀의 높이 값을 나타냄
- automaticDimension은 테이블 뷰의 rowHeight 속성에 대입되어 높이 값이 동적으로 설정될 것을 테이블 뷰에 알려주는 역할을 함
- estimatedRowHeight 속성을 사용하여 임시로 적용될 높이값을 설정하고, rowHeight 속성에 automaticDimension 값을 대입하여 셀의 높이를 동적으로 제어하도록 할 것임을 테이블 뷰에 알려준다. 이 코드들은 viewWillAppear(_:) 메소드와 같은 적절한 시점에 넣어서 구현해 주면 됨
