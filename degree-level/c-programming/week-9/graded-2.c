#include <stdio.h>
#include <math.h>
#include <stdlib.h>


typedef struct Point{
    int x;
    int y;
    struct Point* next;
} Point;

typedef struct{
    Point* points;
} PolyLine;



void add_point(PolyLine* line, int x, int y){
    Point* new_pptr = (Point*) malloc(sizeof(Point));
    new_pptr->x = x;
    new_pptr->y = y;
    new_pptr->next = NULL;

    if (line->points == NULL) {
        line->points = new_pptr;
        return;
    }

    Point* pptr = line->points;
    while (pptr->next != NULL) {
        pptr = pptr->next;
    }
    pptr->next = new_pptr;
}


int manhattan_distance(PolyLine* line) {
    Point* pptr = line->points;
    Point* pptr2 = pptr->next;
    int total = 0;

    while (pptr2 != NULL) {
        total += abs(pptr->x - pptr2->x) + abs(pptr->y - pptr2->y);
        pptr = pptr2;
        pptr2 = pptr2->next;
    }

    return total;
}

void print_line(PolyLine* p){
    Point* current = p->points;
    while(current!=NULL){
        printf("(%d,%d)->",current->x, current->y);
        current = current->next;
    }
    printf("END\n");
}

int main(){
    int x,y;
    int read_next;
    PolyLine line = {NULL};
    while(scanf("%d", &read_next) && read_next)
    {
        scanf("%d %d", &x, &y);
        add_point(&line,x,y);
    }
    print_line(&line);
    printf("%d\n", manhattan_distance(&line));
    
    return 0;
}