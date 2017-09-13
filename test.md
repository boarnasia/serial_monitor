![Alt text](https://g.gravizo.com/source/custom_test01?https%3A%2F%2Fraw.githubusercontent.com%2Fboarnasia%2Fserial_monitor%2Fmd_uml_test%2Ftest.md)

<details>
<summary></summary>
custom_test01
@startuml;
actor User;
participant "First Class" as A;
participant "Second Class" as B;
participant "Last Class" as C;
User -> A: DoWork;
activate A;
A -> B: Create Request;
activate B;
B -> C: DoWork;
activate C;
C -> B: WorkDone;
destroy C;
B -> A: Request Created;
deactivate B;
A -> User: Done;
deactivate A;
@enduml
custom_mark13
</details>
