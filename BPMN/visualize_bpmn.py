import bpmn_python.bpmn_diagram_rep as bpmn_diagram_rep
import bpmn_python.bpmn_diagram_layouter as bpmn_diagram_layouter
import bpmn_python.bpmn_diagram_visualizer as bpmn_diagram_visualizer

def visualize_bpmn(xml_string):
    diagram = bpmn_diagram_rep.BpmnDiagramGraph()
    diagram.from_xml(xml_string)

    layouter = bpmn_diagram_layouter.BpmnDiagramLayouter()
    layouter.layout_diagram(diagram)

    visualizer = bpmn_diagram_visualizer.BpmnDiagramVisualizer()
    visualizer.visualize(diagram, file_path='output.png')

your_xml_string = """
  <?xml version="1.0" encoding="UTF-8"?>
<bpmn:definitions xmlns:bpmn="http://www.omg.org/spec/BPMN/20100524/MODEL" id="Definitions_1">

  <bpmn:process id="Process_1" isExecutable="false">
    <bpmn:startEvent id="StartEvent_1" name="Початок"/>
    <bpmn:sequenceFlow id="SequenceFlow_1" sourceRef="StartEvent_1" targetRef="Task_1"/>
    <bpmn:userTask id="Task_1" name="Авторизація та Вибір Рахунку">
      <bpmn:incoming>SequenceFlow_1</bpmn:incoming>
      <bpmn:outgoing>SequenceFlow_2</bpmn:outgoing>
    </bpmn:userTask>
    <bpmn:sequenceFlow id="SequenceFlow_2" sourceRef="Task_1" targetRef="Task_2"/>
    <bpmn:userTask id="Task_2" name="Вибір Платіжного Методу">
      <bpmn:incoming>SequenceFlow_2</bpmn:incoming>
      <bpmn:outgoing>SequenceFlow_3</bpmn:outgoing>
    </bpmn:userTask>
    <bpmn:sequenceFlow id="SequenceFlow_3" sourceRef="Task_2" targetRef="Task_3"/>
    <bpmn:userTask id="Task_3" name="Підтвердження Данних та Суми">
      <bpmn:incoming>SequenceFlow_3</bpmn:incoming>
      <bpmn:outgoing>SequenceFlow_4</bpmn:outgoing>
    </bpmn:userTask>
    <bpmn:sequenceFlow id="SequenceFlow_4" sourceRef="Task_3" targetRef="Task_4"/>
    <bpmn:userTask id="Task_4" name="Перехід до Платіжного Шлюзу">
      <bpmn:incoming>SequenceFlow_4</bpmn:incoming>
      <bpmn:outgoing>SequenceFlow_5</bpmn:outgoing>
    </bpmn:userTask>
    <bpmn:sequenceFlow id="SequenceFlow_5" sourceRef="Task_4" targetRef="ServiceTask_1"/>
    <bpmn:serviceTask id="ServiceTask_1" name="Виконання Оплати">
      <bpmn:incoming>SequenceFlow_5</bpmn:incoming>
      <bpmn:outgoing>SequenceFlow_6</bpmn:outgoing>
    </bpmn:serviceTask>
    <bpmn:sequenceFlow id="SequenceFlow_6" sourceRef="ServiceTask_1" targetRef="Task_5"/>
    <bpmn:userTask id="Task_5" name="Підтвердження та Оновлення Статусу">
      <bpmn:incoming>SequenceFlow_6</bpmn:incoming>
      <bpmn:outgoing>SequenceFlow_7</bpmn:outgoing>
    </bpmn:userTask>
    <bpmn:sequenceFlow id="SequenceFlow_7" sourceRef="Task_5" targetRef="EndEvent_1"/>
    <bpmn:endEvent id="EndEvent_1" name="Завершення"/>
    <bpmn:sequenceFlow id="SequenceFlow_8" sourceRef="Task_1" targetRef="EndEvent_1"/>
  </bpmn:process>

</bpmn:definitions>

"""

visualize_bpmn(your_xml_string)
