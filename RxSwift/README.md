# RxSwift
> RxSwift를 공부하고 정리한 내용입니다.

## 목차
|#|제목|내용|
|:---:|:---|:---|
|00|👋 [RxSwift](https://github.com/lygon55555/TIL/blob/main/RxSwift/00.%20RxSwift.md)|RxSwift란?|
|01|🔭 [Observables and Observers](https://github.com/lygon55555/TIL/blob/main/RxSwift/01.%20Observables%20and%20Observers.md)|Observable 생성, 구독, Observer|
|02|🧹 [Disposables](https://github.com/lygon55555/til/blob/main/RxSwift/02.%20Disposables.md)|Disposables, 리소스 해제, 실행 취소|
|03|➕ [Operators](https://github.com/lygon55555/til/blob/main/RxSwift/03.%20Operators.md)|연산자(Operators)|
|04|📖 [Subject](https://github.com/lygon55555/til/blob/main/RxSwift/04.%20Subject.md)|`Subject` : PublishSubject, BehaviorSubject, ReplaySubject, AsyncSubject <br/> `Relay` : PublishRelay, BehaviorRelay|
|05|✏️ [Create Operators](https://github.com/lygon55555/til/blob/main/RxSwift/05.%20Create%20Operators.md)|just, of, from - `Observable을 생성하는 연산자` 중에서 가장 단순한 3가지 <br/> range, generate - `정수를 지정된 수만큼 방출`하는 Observable을 생성 <br/> repeatElement - `동일한 요소를 반복적으로 방출`하는 Observable을 생성 <br/> deferred - `특정 조건`에 따라서 Observable을 생성 <br/> create - `Observable이 동작하는 방식을 직접 구현` <br/> empty - `completed 이벤트를 전달`하는 Observable을 생성 <br/> error - `error 이벤트를 전달하고 종료`하는 Observable을 생성|
