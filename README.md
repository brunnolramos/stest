# Teste Spark


 - Qual o objetivo do comando cache em Spark?

Devido ao Spark ser Lazy Evaluation, as transformações somente são executadas quando um ação é acionada.
O uso do comando "cache" ajuda a melhorar a eficiência, pois permite que resultados intermediários possam ser armazenados e reutilizados repetidamente.


 - O mesmo código implementado em Spark é normalmente mais rápido que a implementação equivalente em MapReduce. Por quê?

O principal fator que faz com que o Spark rode mais rápido é devido a sua arquitetura ter sido desenhada para utilizar os dados em memória, ao contrário do MapReduce que acessa e armazena os dados em disco.


 - Qual é a função do SparkContext ?

SparkContext representa a conexão com um cluster Spark e pode ser usado para criar RDDs, acumuladores e variáveis de transmissão nesse cluster.


 - Explique com suas palavras o que é Resilient Distributed Datasets (RDD)

RDD é o princinpal objeto utilizado no processamento dados em Spark.
Tem como objetivo abstrair os objetos distribuídos no cluster.
E possui características semelhantes a tabelas de bancos de dados relacionais, como: estrutura de tabelas, tipos de campos, etc.


 - GroupByKey é menos eficiente que reduceByKey em grandes dataset. Por quê?

"... reduceByKey funciona melhor do que groupByKey, porque tenta aplicar a função de redução localmente antes da fase de reprodução aleatória / redução. GroupByKey forçará uma mistura aleatória de todos os elementos antes do agrupamento."

Referência da resposta: https://stackoverflow.com/questions/24071560/using-reducebykey-in-apache-spark-scala


 - Explique o que o código Scala abaixo faz
```
1. val textFile = sc . textFile ( "hdfs://..." )
2. val counts = textFile . flatMap ( line => line . split ( " " ))
3.           . map ( word => ( word , 1 ))
4.           . reduceByKey ( _ + _ )
5. counts . saveAsTextFile ( "hdfs://..." )
```

O código acima está: 
 * lendo um arquivo do hdfs
 * realizando a quebra das linhas por " " (espaço)
 * adicionando as palavras a uma coleção e realizando o mapeamento de chave e valor
 * agregando os valores através da soma
 * gravando a contagem das palavras num arquivo no HDFS.


** Referências **

https://data-flair.training/blogs/apache-spark-lazy-evaluation/
https://www.infoq.com/br/articles/mapreduce-vs-spark/
https://www.devmedia.com.br/introducao-ao-apache-spark/34178
https://spark.apache.org/docs/2.3.0/api/java/org/apache/spark/SparkContext.html
https://stackoverflow.com/questions/24071560/using-reducebykey-in-apache-spark-scala
