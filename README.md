<!-- markdownlint-configure-file {
  "MD013": {
    "code_blocks": false,
    "tables": false
  },
  "MD033": false,
  "MD041": false
} -->

<div align="center">

# Compressor Python LZ77


####


**A simplified implementation of the LZ77 data compression algorithm in python**

The implementation of this algorithm helps to compress data, which allows <br>
 you to increase the speed of file transfer and reduce <br>
 the space it occupies on the hard disk.


</div>


### *Step 1: Clone repository*

```sh
git clone https://github.com/AlekseyKlevtsov/LZ77Compressor.git
```
![Снимок экрана 2022-01-13 030553](https://user-images.githubusercontent.com/80210745/149242900-2d1e3c7a-1bd0-4907-85ae-b6974ab7f6f9.png)


### *Step 2: Usage*

#### *Encode file*

```sh
main.py compressor [path] [path]
```

![Снимок экрана 2022-01-13 030659](https://user-images.githubusercontent.com/80210745/149242982-9a4176ed-2f68-4ae5-8080-ca96025468b8.png)


#### *Decode file*

```sh
main.py decompressor [path] [path]
```

![Снимок экрана 2022-01-13 031652](https://user-images.githubusercontent.com/80210745/149243431-6dbb53e4-e4db-48e1-819c-24f56ece7a7d.png)



#### *Compress text*

```sh
main.py text -c
```

![Снимок экрана 2022-01-13 030903](https://user-images.githubusercontent.com/80210745/149243133-69ac1562-4250-424c-abbd-af6f98f7f955.png)


#### *Decompress text*

```sh
main.py text -d
```

![Снимок экрана 2022-01-13 031008](https://user-images.githubusercontent.com/80210745/149243139-75c17757-db5d-472a-8f0c-5b8b9d7887b1.png)


#### *Сall for help*

```sh
main.py --help
```

![Снимок экрана 2022-01-13 031027](https://user-images.githubusercontent.com/80210745/149243058-3df92dc6-212b-4e04-b874-44bec6451fb3.png)

#### *Вisplay documentation*

```sh
main.py documentation
```
![Снимок экрана 2022-01-13 031103](https://user-images.githubusercontent.com/80210745/149243053-d753da17-ab1f-49d0-83a8-d984dddb0d04.png)

## Authors

* **Aleksey klevtsov** - [GitHub](https://github.com/AlekseyKlevtsov)


