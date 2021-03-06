# CHAPTER 02 – UI 커스터마이징(1) : 스토리보드와 이별하기

# 2.1 커스터마이징의 개념

## 2.1.1 iOS 프로그래밍에서 UI 커스터마이징이란?

- 윈도우는 iOS에서 디바이스의 스크린을 빈틈없이 채우기 위한 객체로, 항상 유저 인터페이스 표현 계층의 최상위에 위치한다. 뷰의 일종이지만 직접 콘텐츠를 가지지는 않으며 콘텐츠를 가진 뷰를 내부에 배치하여 화면에 출력하는 역할만 한다. 화면이 전환되더라도 단지 윈도우 내부에 배치된 뷰 콘텐츠만 변경될 뿐, 윈도우 객체 자체는 전환되지 않는다.
- 뷰는 콘텐츠를 담아 이를 스크린 상에 표시하고, 사용자의 입력에 반응하는 객체이다.
- 윈도우와 뷰 사이는 뷰 컨트롤러를 통해 연결됨. 뷰 컨트롤러는 뷰의 계층을 관리하여 윈도우에 전달하고, 모바일 디바이스에서 감지된 터치 이벤트를 윈도우로부터 전달받아 처리하는 역할을 한다.

2.2.1 뷰 컨트롤러

- 뷰 컨트롤러는 항상 루트 뷰에 대한 참조를 가지고 있기 때문에 뷰 컨트롤러로부터 가장 하위의 서브 뷰에 이르기까지 계층 구조를 따라 참조 관계가 체인처럼 이어진다. 이 덕분에 뷰 컨트롤러가 하위의 모든 뷰에 대한 참조를 가지고 있지 않아도 모든 뷰 계층에 접근할 수 있다.

## 2.2.2 뷰(View)

- 뷰는 다양한 환경 요소들을 종합하여 객체들이 화면에 어떻게 구현될지 결정한 다음, 이를 슈퍼 뷰로 전달한다. 슈퍼 뷰는 이를 받아 자신의 슈퍼 뷰에게 전달함. 최종적으로 루트 뷰는 계층을 거슬러 전달된 모든 서브 뷰와 이들 사이의 상대적 레이아웃을 종합하여 하나의 씬으로 제작한 다음, 윈도우 객체에 전달한다. 여기까지 진행되면, 비로소 우리가 보는 하나의 화면이 완성되어 디바이스에 출력됨.
- 클래스의 상속 특성에 따라 부모 클래스를 상속받는 것은 부모의 부모 클래스까지 함께 상속받는다는 것을 의미
- iOS에서 뷰는 기준점에 의해 위치가 결정됨. 기준점은 사각형의 좌측 꼭지점이다.
- iOS에서 좌표축은 화면의 좌측 모서리를 원점 (0, 0)으로 하여 x, y 좌표축이 각각 오른쪽과 아래쪽으로 뻗어나가는 형태를 가짐.
- 위치를 나타낼 때에는 CGPoint 구조체를 사용하는데 CGPoint 구조체는 CGFloat 타입의 실수값을 가지는 x, y 변수와 두 가지 초기화 구문으로 이루어짐
- CGPoint는 CoreGraphics라는 프레임워크에서 제공하는 구조체이고 UIKit 프레임워크에 CoreGraphics 라이브러리가 포함되어 있다.
- CGRect는 사각형을 표현하기 위해 필요한 x, y 좌표를 CGPoint 객체에 담아 origin 프로퍼티에 저장하고, 너비와 길이는 CGSize 객체에 담아 size 프로퍼티에 저장함
- frame은 뷰의 위치와 크기를 저장하는 데에 사용되는 속성이다. 뷰는 CGRect 인스턴스로 정의된 사각 영역 정보 (x, y, width, height)를 frame 속성에 대입하여 자기 자신이 점유할 영역을 결정한다.
- frame 속성의 x, y 값을 이용하여 뷰를 원하는 다른 위치로 이동시킬 수 있다.
- 실제로 옮겨진 뷰의 위치를 계산할 때에는 주의해야 한다. frame 속성의 좌표값이 가리키는 위치는 자신의 상위 뷰를 기준으로 하는 상대적인 값이기 때문. 뷰는 화면 원점을 기준으로 하는 절대 좌표계가 아니라 부모 뷰의 위치를 기준으로 자신의 좌표를 계산하는 상대 좌표계를 적용함
- frame의 좌표 기준은 슈퍼 뷰이다. 슈퍼 뷰의 기준점을 원점 (0, 0)으로 하여 자신의 좌표를 계산함. 하지만 bounds에서 좌표 기준은 자기 자신이다.
- bounds 속성은 뷰의 내부에 있는 개체와의 관계에서 사용한다. 슈퍼 뷰가 서브 뷰에게 제공하는 좌표는 bounds 속성의 좌표이고, 서브 뷰는 이 좌표를 기준으로 자신의 frame 속성을 설정한다.
- bounds 속성의 (x, y) 좌표를 강제로 변경해 버리면 좌표를 변경한 뷰의 위치는 변하지 않지만 그 뷰의 내부에 정의된 서브 뷰들은 슈퍼 뷰가 이동한 것으로 인식하고 자신들의 위치를 그에 따라 이동시킴. 이는 자식 뷰가 기준으로 삼는 부모 뷰의 좌표 속성이 bounds 이기 때문이다. 이 같은 특성을 이용하면 외부 뷰는 그대로 둔 채 내부 뷰만 위치를 이동시키거나 스크롤 기능을 처리하도록 할 수도 있음. 주로 이미지 뷰어에서 큰 이미지를 드래그해서 볼 수 있도록 처리할 때 사용하는 방법이다.

# 2.3 커스텀 코드로 화면 구현하기

## 2.3.1 뷰 컨트롤러에 버튼 추가하기

- center 속성은 객체의 중심 좌표를 지정하는 역할로, CGPoint 타입으로 정의됨
- origin 좌표가 결정되면 center 속성값도 자동으로 결정되고, 반대로 center 속성의 좌표가 결정되면 frame.origin 속성도 이에 따라 바뀌게 됨

## 2.3.2 이벤트 처리와 액션 메소드의 연결

- addTarget(_:action:for:) 메소드는 모두 세 개의 매개변수를 가짐.
    - 첫 번째 매개변수 : target 호출할 메소드가 정의된 인스턴스를 가리킴. 같은 뷰 컨트롤러 내에 액션 메소드가 작성되어 있으면 self를 인자값으로 전달하고 다른 뷰 컨트롤러에 속한 메소드를 호출해야 한다면, 해당 뷰 컨트롤러의 인스턴스를 인자값으로 넣어주면 됨. 간혹 액션 메소드를 뷰 컨트롤러가 아니라 뷰에 정의하는 경우도 있는데, 이때에는 뷰 컨트롤러의 인스턴스가 아니라 뷰의 인스턴스를 인자값으로 전달해야 함. 유연하게 인스턴스 타입을 사용할 수 있도록 target 매개변수의 타입은 Any로 정의됨
    - 두 번째 매개변수 : action 호출할 메소드를 지정하는 매개변수이다. 매개변수의 타입은 Selector이고 함수를 직접 지정하는 기능을 가진 일종의 함수 선택자로, 실제로 사용할 때에는 #selector(함수이름) 형태로 작성하면 됨.  
    특정 형식으로 정의된 메소드만 인자값으로 사용할 수 있다는 것에 주의해야 함. 지정된 메소드를 호출할 때 시스템은 이 메소드를 호출한 객체의 정보를 인자값으로 전달함. 이 값을 받기 위해 해당 메소드는 하나의 매개변수를 가지고 있어야 하며, 또한 객체 참조를 전달받을 수 있도록 특정 타입으로 정의되어 있어야 함.
    - 세 번째 매개변수 : for 액션 메소드의 실행 조건을 지정하는 매개변수이다.
- Selector는 본래 오브젝티브-C에서 클래스 메소드의 이름을 가리키는 데 사용되는 참조 타입이다. 동적 호출 등의 목적으로 @selector() 어트리뷰트에 메소드 이름을 인자값으로 넣어 전달하면 이를 내부적으로 정수값으로 매핑해서 처리하는 형태였음. 이것이 스위프트로 넘어오면서 구조체 형식으로 정의되고, #selector() 구문을 사용하여 해당 타입의 값을 생성할 수 있게 됨.
- Swift4부터는 Selector 타입으로 전달할 메소드를 작성할 때 반드시 @objc 어트리뷰트를 붙여주어야 하는데 이것은 오브젝티브-C와의 호환성을 위한 것이다.
- #selector() 구문을 작성할 때에는 인자값에 메소드 시그니처를 정확하게 넣어주는 것이 원칙이다.
- 오버로딩된 메소드는 #selector()의 인자값으로 사용할 수 없을 뿐만 아니라, 오브젝티브-C 기반 클래스를 상속받거나 @objc 어트리뷰트를 건 상태에서 메소드 오버로딩은 원천적으로 불가능하다.
- Event 객체에는 필요한 모든 이벤트 조건들이 열거형 아이템으로 정의되어 있고 이 값들은 addTarget(_:action:for:) 메소드의 세 번째 인자값으로 사용될 “액션 메소드가 실행되는 조건값”이다.
- btnOnClick(_ sender: Any) 메소드는 사용자가 버튼을 터치했을 때 반응할 액션 메소드이다. 이 메소드는 다음과 같은 형식 요건을 반드시 만족해야 함
    - 매개변수 : 이벤트가 발생한 객체 정보를 전달받을 수 있도록 Any 혹은 해당 객체 타입의 첫 번째 매개변수를 정의해야 한다.
    - 첫 번째 매개변수의 타입은 Any, AnyObject 또는 호출한 객체의 타입이어야 한다.
    - @objc 어트리뷰트를 붙여 오브젝티브-C에서도 인식할 수 있도록 해야 한다.
- 액션 메소드는 반드시 하나의 매개변수를 가져야 하며, Any, AnyObject 또는 호출한 객체의 타입으로 선언되어야 함. 이는 호출한 객체의 정보를 인자값으로 전달하기 위함이다.
- 하나의 액션 메소드를 여러 객체가 호출하는 상황이라면 Any 또는 AnyObject로 매개변수를 선언하는 것이 좋음. 스위프트에서 AnyObject는 범용 클래스 타입으로 모든 클래스 타입에 사용할 수 있으며, Any는 범용 객체 타입으로 클래스나 구조체를 포함한 모든 타입의 객체에 사용할 수 있기 때문이다.

## 2.3.3 아웃렛 변수의 구현

- 선언과 초기화를 분리하여 viewDidLoad 메소드 내에서 초기화 구문을 작성할 경우, 레이블 인스턴스가 생성되는 시점은 뷰 컨트롤러의 뷰가 로드될 때이다. → 실제로 뷰 컨트롤러가 화면에 처음 표시되는 시점에 인스턴스가 생성됨
- 하지만 멤버 변수를 선언하면서 동시에 객체를 초기화하면 뷰 컨트롤러의 인스턴스가 생성되는 시점에 레이블 인스턴스도 함께 생성됨. 만약 뷰 컨트롤러의 인스턴스만 생성한 후 화면으로 이동하지 않는다면 생성된 레이블 인스턴스가 메모리만 차지하는 결과가 생긴다. 이는 결국 메모리의 낭비로 이어짐. 반면 viewDidLoad 메소드 내에서 초기화를 처리하면 뷰 컨트롤러가 화면에 표시될 때에야 비로소 레이블 객체가 생성되므로 메모리 소모를 줄일 수 있다.
- 반드시 필요한 경우를 제외하고는 가급적 사용하기 직전에 인스턴스를 생성하여 메모리를 할당받는 것이 메모리 사용 효율 면에서 좋다.

## 2.3.4 입력폼의 구현

- systemFont(ofSize:) : 폰트 크기 조절
- boldSystemFont(ofSize:) : 폰트 크기와 볼드 설정
- UIFont(name:size:) : 폰트의 종류까지 지정
- familyNames : 폰트 패밀리 목록을 확인
- Post Script Name이라고 부르는 실제 폰트의 이름을 얻기 위해서는 fontNames(forFamilyName:)을 호출해야 함
- adjustFontSizeToFitWidth는 입력된 문자열의 폰트 사이즈를 텍스트 필드의 너비에 맞게 자동으로 조정해 주는 유용한 속성이다. true로 설정한 텍스트 필드는 입력된 문자열의 길이와 텍스트 필드의 너비에 따라 폰트 사이즈가 다르게 적용됨
- UIColor 클래스를 이용하면 단순 색상 외에도, 인자값으로 입력된 이미지를 패턴 처리하여 배경 이미지를 만들어 낼 수도 있음. 여기서 패턴 처리한다는 것은 이미지가 반복해서 표현된다는 뜻이다.
