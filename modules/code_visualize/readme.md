### CodeBase Visualization Tools


#docker


docker-compose-viz: Docker Compose Visualization

[https://github.com/pmsipilot/docker-compose-viz](https://github.com/pmsipilot/docker-compose-viz)

```Bash
# Usage
docker run \--rm \-it \--name dcv \-v $(pwd):/input pmsipilot/docker-compose-viz render \-m image docker-compose.yml

```


#python #JS #PHP #Ruby


Code2flow

[https://github.com/scottrogowski/code2flow](https://github.com/scottrogowski/code2flow)

```Bash
# usage
code2flow code2flow/engine.py code2flow/python.py --target-function=code2flow --downstream-depth=3
```


#python


pyan - python code visualization

[https://github.com/davidfraser/pyan](https://github.com/davidfraser/pyan)

```Bash
pyan *.py --uses --no-defines --colored --grouped --annotated --svg >myuses.svg
```


pipdeptree - python dependency visualization  
  
[https://pypi.org/project/pipdeptree/](https://pypi.org/project/pipdeptree/)

```Bash
pipdeptree --graph-output svg > dependencies.svg
```


Bazel

[https://blog.bazel.bild/2015/06/17/visualize-your-build.html](https://blog.bazel.build/2015/06/17/visualize-your-build.html)

```Bash
bazel query 'deps(//:main)' --output graph > dependencies.in
dot -Tpng < dependencies.in > dependencies.svg
```

u
