![Alt text](https://g.gravizo.com/source/custom_test01?https://raw.githubusercontent.com/boarnasia/serial_monitor/md_uml_test/test.md)

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
