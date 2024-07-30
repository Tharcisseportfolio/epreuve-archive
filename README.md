- How to query this database

grade : Getting the grade

grade = Grade.objects.all()
grade = Grade.objects.get(name='9') // for 9th grade

// Getting all courses
courses = Course.objects.all()

//get specific course
Course.objects.get(name="Biology thematique")
returning a course: <Course: Biology thematique>

//get a querySet for a specific course
// I can use filter
Course.objects.filter(name="Biology thematique")
returning a query set for the course: <QuerySet [<Course: Biology thematique>]>

....etc..

//Defining relationship or ORM(Objects Relational Model)

1. Course: relationship with:
    - grade : in which grade is this course taught
    - section : in which section
2. Epreuve : Relationship with Course
    - Course : In which course was this epreuve from
    - To remember: The course can also give us the grade and the section

2.Exetat : Relationship with Course
    - Course : In which course was this exetat from
    - To remember: The course can also give us the grade and the section

//How to query these models with these relationship

1. Grade

- Getting the grade for a specific course

    course = Course.objects.get(name="Biology thematique")
    course.grade // to get the grade
    returns : <Grade: 3ème Post Fondamental(Finalistes)>

- Getting the grade for a specific epreuve

    1. we can filter for each course since a course register the grade and the each epreuve is related to the course

    -  epreuve = Epreuve.objects.get(name="Epreuve d'anglais 2023") : getting a specific epreuve
    - course = epreuves.course : to get the course 
    - grade = course.grade
    - returning : <Grade: 3ème Post Fondamental(Finalistes)>

....EVERYTHING ELSE CAN BE DONE THE SAME WAY