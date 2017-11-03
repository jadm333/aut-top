###Cargar datos
using TopicModelsVB
import Distributions.sample
#Arreglar direccion
corp = readcorp(:mac)

corp.docs = vcat([sample(filter(doc -> round(doc.stamp / 100) == y, corp.docs), 400, replace=false) for y in 1984:2005]...)

fixcorp!(corp, abr=100, len=10) # Remove words which appear < 100 times and documents of length < 10.

basemodel = LDA(corp, 9)
train!(basemodel, iter=150, chkelbo=151)

# training...

model = DTM(corp, 9, 200, basemodel)
train!(model, iter=10) # This will likely take about an hour on a personal computer.
                       # Convergence for all other models is worst-case quadratic,
                       # while DTM convergence is linear or at best super-linear.
# training...
