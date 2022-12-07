#include <nombreDeLibreria.extension>
int  MD1;
string  MD2;
MD2:="valor";
MD1:=3;
void setup(){
pinMode(MD1, OUTPUT);
pinMode(MD2, OUTPUT);

}
void loop(){
avanzar();
giro_izquierda();
parar();

}
