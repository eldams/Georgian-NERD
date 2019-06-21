# Georgian-NER-EL

This is an alpha version of what could become a named entity tagger and linker. For lazy people, just clone repository and try this:

```echo "მისი თქმით, ერთობლივი ანტიტერორისტული ოპერაციები პანკისის ხეობაში არ იგეგმება." | python predict.py```

This requires quite standard packages installed as scikit.

Don't expect good results, since the current model has be learnt using 

If you'd like to learn a new model, you'll have to:

- have some annotated data
- find a corpus to learn embeddings
