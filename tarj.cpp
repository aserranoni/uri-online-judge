#include<cstdio>
#include<cstring>
#include<map>
#include<set>
#include<stack>
#include<vector>
using namespace std;

#define MAX_VERT 5001

stack<int> mystack ;
bool on_stack[MAX_VERT] ={false}, cont = true;
int num_comps=1, id=0, ids[MAX_VERT], low[MAX_VERT], components[MAX_VERT];
map<int, set<int>> grafo;

  void read_instance(){
  grafo.clear();
  num_comps =1;
  int V, E, i, out, in;
  scanf("%d %d" , &V, &E);
  if (V != 0){
    for(i=0; i< E ; i++){
      scanf("%d%d", &out, &in);
      printf("out = %d e in = %d\n", out, in);
      grafo[out].insert(in);
    }
  }
  else{
    cont = false;
  }
}

void dfs_visit(int at){
  mystack.push(at);
  on_stack[at] = true;
  id++;
  low[at] = id;
  ids[at] = id;
  set<int>::iterator to ;
  for(to= grafo[at].begin() ;to!= grafo[at].end() ;++to){
    if(ids[*to] == -1){
      printf("Visiting vertex %d\n", *to);
      dfs_visit(*to);
    }
    if(on_stack[*to] == true){
      low[at] = min(low[*to],low[at]);
    }
  }
  if(ids[at]==low[at]){
    while(mystack.empty() == false){
      int node = mystack.top();
      //printf("node = %d\n", node);
      //printf("num_comps = %d\n", num_comps);
      mystack.pop();
      on_stack[node]=false;
      components[node] = num_comps;
      if(node == at){
        break;
      }
    }
    num_comps++;
  }
}

void find_components(){
  int n = grafo.size();
  for (int i = 1; i<=n ; i++){
    ids[i]=-1;
  }
  id =0;
  for(int i =1; i <= n ; i++){
    if(ids[i] == -1){
      printf("Visiting vertex %d\n", i);
      dfs_visit(i);
  }
  }
}

void print_components(){
  int n = grafo.size();
  for(int i=1; i<=n; i++){
    printf("%d ",components[i]);
      }
  printf("\n");
}

void print_bottom(){
  int k = grafo.size();
  bool bottom[k] ={true};
  for(int i=1; i<=k; i++){
    set<int>::iterator j;
    for( j=grafo[i].begin(); j!=grafo[i].end(); ++j){
      if(components[*j] != components[i]){
        bottom[i] =false;
    }
  }
  }
  for(int i=1; i<=k; i++){
    if(bottom[i] == true){
      printf("%d" , i);
        }
  }
  printf("\n");
}

int main(){
  while(cont == true){
    read_instance();
    find_components();
    print_components();
    //printf("proximo grafo\n");
  }
 return 0;}
