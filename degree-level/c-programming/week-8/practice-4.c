#include <stdio.h>


typedef enum {
        SQUARE,
        RECTANGLE,
        CIRCLE,
        TRIANGLE
} ShapeId;


typedef union {
    ShapeId id;

    struct {
        ShapeId id;
        float side;
    } square;

    struct {
        ShapeId id;
        float length;
        float breadth;
    } rectangle;

    struct {
        ShapeId id;
        float radius;
    } circle;

    struct {
        ShapeId id;
        float base;
        float height;
    } triangle;
} Shape;


float compute_area(Shape* shape) {
    float area;

    switch (shape->id) {
        case SQUARE:
            area = shape->square.side * shape->square.side; break;
        case RECTANGLE:
            area = shape->rectangle.length * shape->rectangle.breadth; break;
        case CIRCLE:
            area = 3.14 * shape->circle.radius * shape->circle.radius; break;
        case TRIANGLE:
            area = 0.5 * shape->triangle.base * shape->triangle.height; break;
    }

    return area;
}


float combined_area(Shape shapes[], int n) {
    float out = 0;
    for (int i = 0; i < n; i++) {
        out += compute_area(&shapes[i]);
    }

    return out;
}


void read_shape(Shape *shape){
    scanf("%u", &shape->id);
    switch(shape->id){
        case SQUARE:
            scanf("%f", &shape->square.side);
            return;
        case RECTANGLE:
            scanf("%f %f", &shape->rectangle.length, &shape->rectangle.breadth);
            return;    
        case CIRCLE:
            scanf("%f", &shape->circle.radius);
            return;
        case TRIANGLE:
            scanf("%f %f", &shape->triangle.base, &shape->triangle.height);
    }
}


void read_shapes(Shape shapes[], int n) {
    for (int i=0;i<n;i++){
        read_shape(shapes+i);
    }
}


int main() {
    int n; 
    scanf("%d",&n);
    Shape shapes[n];
    read_shapes(shapes,n);
    printf("%.2f", combined_area(shapes, n));
    return 0;
}
