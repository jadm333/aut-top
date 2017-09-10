setwd("/root/aut-top")
do.call(file.remove, list(list.files("Archivos_csv", full.names = TRUE)))
ids_twitter <- read.csv("twitter_in_group.csv", row.names=NULL, sep="", stringsAsFactors=FALSE)
##Quitar duplicados


ids_twitter = ids_twitter[!duplicated(ids_twitter),]

require("RMySQL")
###### PErfiles
drv = dbDriver("MySQL")
query = paste0("SELECT * 
               FROM  `twitter` 
               WHERE id_twitter IN (SELECT id_twitter 
               FROM  `twitter_in_group` 
               WHERE id_twitter_group IN (52,58,56,55,57,53,85,86));
               ")
con = dbConnect(drv, user="root",password="56653356", dbname="conversia", host="localhost")
dbGetQuery(con, "SET NAMES utf8mb4")
perfiles = dbGetQuery(con,query)
dbDisconnect(con)
###### Tweets


for(i in 1:length(ids_twitter)){
  query = paste0("SELECT * FROM  `tweet` WHERE id_twitter = ",ids_twitter[i],";")
  con = dbConnect(drv, user="root",password="56653356", dbname="conversia", host="localhost")
  dbGetQuery(con, "SET NAMES utf8mb4")
  data = dbGetQuery(con,query)
  screenname = perfiles[perfiles$id_twitter==ids_twitter[i],2]
  file=paste0("Archivos_csv/",screenname,".csv")
  write.csv(data, file)
  dbDisconnect(con)
  terminado = paste0(i," Terminado: ",screenname)
  print(terminado)
}

