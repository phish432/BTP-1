# BTP-1

Advisor: Chiranjeevi Yarra

Team: Agrim Rawat, Arnav Pandey

# How To Use

1. Install [espnet](https://espnet.github.io/espnet/installation.html) and `requiremets.txt`.

2. Unzip `data.zip`

```
unzip data.zip
```

3. Prepare data

```
python dataPreparation.py
```

4. Run `s2t.py` (stages 2, 3, 4)

```
python s2t.py
```

or

```
python s2t.py 4
```

to run only stage 4 (Data Processing).


5. Run `asralign.py` (stages 2, 3, 4)

```
python asralign.py
```

or

```
python asralign.py 4
```

to run only stage 4 (Data Processing).