// INCOMPLETE

#include <stdio.h>
#include <math.h>


typedef enum {
    THEORY=1,
    PROGRAMMING,
    PROJECT
} CourseType;


typedef union {
    struct {
        int quiz1;
        int quiz2;
        int assignments;
        int final_exam;
    } theory;
    
    struct {
        int quiz1;
        int oppe1;
        int oppe2;
        int assignments;
        int programming_assignments;
    } programming;

    struct {
        int viva1;
        int viva2;
        int final_project;
    } project;
} Grading;


typedef struct {
    char course_id[10];
    CourseType course_type;
    Grading grading;
    int score;
} Course;


void compute_score(Course* c) {
    switch (c->course_type) {
        case THEORY:
            c->score = 0.15*c->grading.theory.quiz1 + 0.15*c->grading.theory.quiz2 + 0.1*c->grading.theory.assignments + 0.6*c->grading.theory.final_exam;
            break;
        case PROGRAMMING:
            c->score = 0.1*c->grading.programming.quiz1 + 0.3*c->grading.programming.oppe1 + 0.3*c->grading.programming.oppe2 + 0.1*c->grading.programming.assignments + 0.2*c->grading.programming.programming_assignments;
            break;
        case PROJECT:
            c->score = 0.25*c->grading.project.viva1 + 0.25*c->grading.project.viva2 + 0.25*c->grading.project.final_project;
            break;
    }
}

void read_course(Course *c){
    scanf("%s", c->course_id);
    scanf("%d", &c->course_type);
    Grading* g = &c->grading;
    switch(c->course_type){
        case THEORY:
            scanf(
                "%d %d %d %d", 
                &g->theory.quiz1, 
                &g->theory.quiz2, 
                &g->theory.assignments, 
                &g->theory.final_exam
            );
            break;
        case PROGRAMMING:
            scanf(
                "%d %d %d %d %d",
                &g->programming.quiz1,
                &g->programming.oppe1,
                &g->programming.oppe2,
                &g->programming.assignments,
                &g->programming.programming_assignments
            );
            break;    
        case PROJECT:
            scanf(
                "%d %d %d",
                &g->project.viva1,
                &g->project.viva2,
                &g->project.final_project
            );
    }
}

int main()
{
    Course course;
    read_course(&course);
    compute_score(&course);
    printf("%s - %d", course.course_id, course.score);
    return 0;
}
