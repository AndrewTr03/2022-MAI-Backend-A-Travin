1.  Установлен Nginx
    Установлен Gunicorn   
2.  Nginx настроен на отдачу статических файлов по пути http://server_name:80/public/ (Файлы Default и nginx.conf)
3.  Создан и запущен с помощью gunicorn файл простейшего WSGI-приложения(Расположено в папке gunicorn)
4.  Nginx настроен на проксирование запросов на сервер gunicorn (Файлы Default и nginx.conf)
5.  Проведено тестирование производительности с помощью ab
    $ ab -n 10 -c 2 -t 1 -v 2 http://10.0.2.15/public/index.html

    Finished 2656 requests


Server Software:        nginx/1.14.0
Server Hostname:        10.0.2.15
Server Port:            80

Document Path:          /public/index.html
Document Length:        192 bytes

Concurrency Level:      2
Time taken for tests:   1.000 seconds
Complete requests:      2656
Failed requests:        0
Total transferred:      1150048 bytes
HTML transferred:       509952 bytes
Requests per second:    2655.58 [#/sec] (mean)
Time per request:       0.753 [ms] (mean)
Time per request:       0.377 [ms] (mean, across all concurrent requests)
Transfer rate:          1122.92 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.4      0       8
Processing:     0    1   0.7      0       9
Waiting:        0    0   0.4      0       9
Total:          0    1   0.9      0      10
WARNING: The median and mean for the processing time are not within a normal deviation
        These results are probably not that reliable.
WARNING: The median and mean for the total time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      1
  75%      1
  80%      1
  90%      1
  95%      2
  98%      4
  99%      5
 100%     10 (longest request)


$ ab -n 10 -c 2 -t 1 -v 2 http://10.0.2.15/backend
Finished 2403 requests


Server Software:        nginx/1.14.0
Server Hostname:        10.0.2.15
Server Port:            80

Document Path:          /backend
Document Length:        194 bytes

Concurrency Level:      2
Time taken for tests:   1.000 seconds
Complete requests:      2403
Failed requests:        0
Non-2xx responses:      2403
Total transferred:      956394 bytes
HTML transferred:       466182 bytes
Requests per second:    2401.82 [#/sec] (mean)
Time per request:       0.833 [ms] (mean)
Time per request:       0.416 [ms] (mean, across all concurrent requests)
Transfer rate:          933.52 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.5      0       8
Processing:     0    1   0.9      0      12
Waiting:        0    0   0.4      0       7
Total:          0    1   1.1      0      12
WARNING: The median and mean for the processing time are not within a normal deviation
        These results are probably not that reliable.

Percentage of the requests served within a certain time (ms)
  50%      0
  66%      1
  75%      1
  80%      1
  90%      1
  95%      3
  98%      4
  99%      6
 100%     12 (longest request)



$ ab -n 10 -c 2 -t 1 -v 2 http://127.0.0.1:8000/
    Finished 1043 requests


Server Software:        gunicorn/19.7.1
Server Hostname:        127.0.0.1
Server Port:            8000

Document Path:          /
Document Length:        21 bytes

Concurrency Level:      2
Time taken for tests:   1.000 seconds
Complete requests:      1043
Failed requests:        0
Total transferred:      174348 bytes
HTML transferred:       21924 bytes
Requests per second:    1042.85 [#/sec] (mean)
Time per request:       1.918 [ms] (mean)
Time per request:       0.959 [ms] (mean, across all concurrent requests)
Transfer rate:          170.24 [Kbytes/sec] received

Connection Times (ms)
              min  mean[+/-sd] median   max
Connect:        0    0   0.2      0       5
Processing:     0    2   1.7      1      13
Waiting:        0    1   1.0      0      10
Total:          0    2   1.7      1      13

Percentage of the requests served within a certain time (ms)
  50%      1
  66%      2
  75%      2
  80%      3
  90%      4
  95%      5
  98%      7
  99%      9
 100%     13 (longest request)

