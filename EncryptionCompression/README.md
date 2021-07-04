Utility that will detect encrypted/compressed files in a specified directory.

Command line arguments:

(The parameters for sorting are different from those given in the task. I don't think that
it would be a big deal)

  a. -d, --dir: specifies the path to directory where to look for encrypted/compressed files. Default - current directory.
  b. -c, --confidence: specifies the threshold level of confidence (in percents from 0 to 100) to treat a certain file as encryped/compressed. Default - 80%.
  c. -ds, --descending: all files in the program output should be sorted by confidence level descending (from high to low).
  d. -as, --ascending: all files in the program output should be sorted by confidence level ascending (from low to high).
  e. -p, --print-confidence: print the confidence level along with the file name.
  f. -h, --help: print help message for all available options.

Tests:
1. 
  D:\Courses\UnderDefense\Python\hometask5>py DetectEncrypted.py -c 40 -as --dir D:\Courses\JSCore\repository\JavaScript_lesson_04
  README.md
  task3.js
  task4.js
  task7.js
  task6.js
  task5.js
  task1.html
  task2.html
2. 
  D:\Courses\UnderDefense\Python\hometask5>py DetectEncrypted.py -c 40 --print-confidence -ds -d D:\Courses\JSCore\repository\JavaScript_lesson_16
  63% task.js
  62% ajax.html
  62% server.js
  60% package-lock.json
  52% README.md
  50% package.json
