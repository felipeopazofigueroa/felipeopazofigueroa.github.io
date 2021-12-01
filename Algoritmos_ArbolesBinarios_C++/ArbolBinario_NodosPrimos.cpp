#include <iostream>
#include <bits/stdc++.h>

using namespace std;

//ENUNCIADO 2 - Nombres: Miguel Jaime - Oliver Lillo - Felipe Opazo
 
// Estructura de datos que almacena el peso de los nodos, y su puntero izquierdo y derecho.
struct Nodo{
    int peso;
    Nodo *pIzq, *pDer;
};

//Se crean 3 contadores y dos vectores que seran utilizados mas adelante para verificar los nodos.
int cont = 0, cont2 = 0, cont3 = 0;
vector <int> vA, vB;


 
/* Se crea una función crearNodo a partir de la estructura "Nodo" que toma un valor como argumento.
Un puntero temporal (temp) crea y almacena un nodo nuevo mediante "new", el cual accedera posteriormente mediante el peso al valor
Y al puntero izquierdo y derecho que tienen un valor nulo*/

Nodo *crearNodo(int valor){
    Nodo *temp = new Nodo;
    temp->peso = valor;
    temp->pIzq = temp->pDer = NULL;
    return temp;
}
 

/*Se crea la funcion getAltura de tipo entero, que toma la raiz del nodo, el nodo y la altura (nivel) del nodo como argumentos.
Esta retornará la altura del nodo si es que esta en el arbol, sino, retorna 0*/

int getAltura(Nodo *raiz, Nodo *nodo, int altura){
    if (raiz == NULL)
        return 0;
    if (raiz == nodo)
        return altura;
 
    // Verifica si el nodo esta en el subarbol izquierdo
    int alturaInf = getAltura(raiz->pIzq,nodo, altura + 1);
    if (alturaInf != 0)
        return alturaInf;
 
    // Retorna si no esta en el subarbol izquierdo
    return getAltura(raiz->pDer, nodo, altura + 1);
}

/*Se crea la funcion anadirPrimosVector la cual segun una raiz, nodo y altura dada, recorrera el arbol y segun por donde pase, ira añadiendo
los nodos primos de el nodo A o B al vector vA o vB mediante push_back con un contador que permite saber por cual rama pasaron; esto servira ya que al
haber agregado los pesos de los nodos en cada uno de los vectores se podra realizar una comparacion entre estos vectores (si poseen los mismos 
valores, son nodos hermanos, no primos; y si no es asi, entonces son nodos primos)*/

void anadirPrimosVector(Nodo* raiz, Nodo *nodo, int altura){
    if (raiz == NULL or altura < 2)
        return;

    if (altura == 2){
        if (raiz->pIzq == nodo or raiz->pDer == nodo){
            return;
        }
        if (raiz->pIzq){
            if(cont2 == 0){
               vA.push_back(raiz->pIzq->peso); 
            }
            else{
               vB.push_back(raiz->pIzq->peso); 
            }
        }
        if (raiz->pDer){
            if(cont2 == 0){
                vA.push_back(raiz->pDer->peso);
                cont2++;
            }
            else{
                vB.push_back(raiz->pDer->peso);
            }
        }
    }

    else if (altura > 2){
        anadirPrimosVector(raiz->pIzq, nodo, altura - 1);
        anadirPrimosVector(raiz->pDer, nodo, altura - 1);
    }
}
 
// Se crea la funcion getSonPrimos de tipo void que podra ayudar a la funcion buscarNodo a determinar si los nodos A y B son primos.
void getSonPrimos(Nodo *raiz, Nodo *nodo){
    int altura = getAltura(raiz, nodo, 1);
    anadirPrimosVector(raiz, nodo, altura);
}

//Se crea la funcion buscarNodo la que ayudara en el main posterior para poder buscar el nodo especificado por el usuario dentro del arbol
//Esta funcion al verificar que el nodo esta en el arbol, verifica que este no sea raiz; si es raiz, imprime que no son primos
//Si no es raiz, entonces verifica que los elementos del vector sean diferentes, si es asi, los nodos son primos, sino, no lo son
//Luego si al recorrer dos veces el ciclo hay al menos un nodo que es raiz, imprime de inmediato que no son nodos primos

void buscarNodo(Nodo *raiz, int valor)
{
	int altNodo = 0;
	Nodo *temp = new Nodo;
	temp = raiz;

	while(temp != NULL){
		altNodo++;
		if(temp->peso == valor){
            //Se ejecuta la funcion getSonPrimos para agregar los nodos primos de los nodos A y B a los vectores segun la altura
            getSonPrimos(raiz, temp);

            //Para determinar si el nodo es hoja (o nodo leaf) ya que no tendra ni hijo izquierdo ni derecho
            if(temp-> pIzq == NULL && temp -> pDer == NULL){
                cont++;

                //Si cont == 2 significa que los dos nodos A y B ingresados son nodos hoja, ya que pasaron por la condicional 2 veces.
                if(cont == 2){
                    //Aca se compara a los dos vectores, si estos son diferentes segun sus elementos agregados previamente, son nodos primos 
                    if(vA != vB){
                        cout<<"\nSon nodos primos!"<<endl;
                    }
                    //Si sus elementos son iguales no son nodos primos, sino que son hermanos ya que tendrian los mismos nodos primos en comun
                    else{
                        cout<<"\nNo son nodos primos!"<<endl;
                    }
                }
                //Este else if significa que si el ciclo while llego a su fin y el contador llego a 1 (osea que habia un nodo que era raiz)
                //o el contador llego a 0 (osea que habian dos nodos raiz), entonces de inmediato no son nodos primos ya que no satisface las condiciones
                else if(temp == NULL & (cont == 1 or cont == 0)){
                    cout<<"\nNo son nodos primos!"<<endl;
                }
            }
            //De otra forma, logicamente establece que si cumple la condicion de arriba de ser nodos hojas, de inmediato no son nodos primos
            //ya que existe al menos una raiz en los nodos A y B
            else{
                cout<<"\nNo son nodos primos ya que existe una raiz!"<<endl;
                cont3++;
            }
			return;
		}
        //Para irse por el subarbol izquierdo
		else if(temp->peso > valor)
			temp = temp->pIzq;
        //Para irse por el subarbol derecho
		else
			temp = temp->pDer;
	}
 
	cout<<"\n No se ha podido encontrar el valor del nodo especificado.\n";
	return;
}

//Funcion mostrarArbol que mostrara el arbol al ejecutar el programa para que asi el usuario elija de que nodos desea comprobar

void mostrarArbol(Nodo *raiz, int cont){
    if(raiz==NULL){
        return;

    }
    else{
        mostrarArbol(raiz->pDer,cont+1);
        for(int i=0;i<cont;i++){
            cout<<"   ";

        }
        cout<<raiz->peso<<endl;
        mostrarArbol(raiz->pIzq,cont+1);
    }
}
 
// Se prueba un main con los nodos que componen el arbol binario, para así luego verificar cuales son los nodos primos de cierto nodo.
//PD: La condicional if del final del main existe en caso de que ambos nodos sean raiz; en este caso, el mensaje se imprimiria dos veces
//gracias al ciclo while, por lo que con el if evitamos que esto pase y tan solo se imprime una vez.

int main(){
    int nodoA, nodoB;
    int dato,opcion,contador=0;
    Nodo *raiz = crearNodo(10);
    raiz->pIzq = crearNodo(5);
    raiz->pDer = crearNodo(20);
    raiz->pIzq->pIzq = crearNodo(3);
    raiz->pIzq->pDer = crearNodo(6);
    raiz->pDer->pIzq = crearNodo(15);
    raiz->pDer->pDer = crearNodo(25);
    cout<<"\nArbol Binario\n";
    mostrarArbol(raiz,contador);
    cout<<"\nSegun el arbol binario planteado, ingrese el nodo A para verificar si son nodos primos: "<<endl;
    cin>>nodoA;
    cout<<"\nIngrese el nodo B para verificar si son nodos primos: "<<endl;
    cin>>nodoB;
    buscarNodo(raiz, nodoA);
    if(cont3 != 1){
        buscarNodo(raiz, nodoB);
    }
    cout<<"\n";

    //Por si se usa el ejecutable del programa, este no se cierre de inmediato una vez que termina de ejecutarse el main
    system("pause");
}