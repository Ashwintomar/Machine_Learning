2+5


#comment


#creating a variable

x <- 2
x <- 3

x


# input some array

y<- c(1,2,3,4,5)

y<- 1:10


x<- y<- 1:10

x3<- seq(5,50,by = 5)

x4<- scan()

#matrix addition

z<- x+y


#Matrix multiplication

z2<- x*y

#Its a case sensitive language

X <- 10

#list all var


ls()


#removing elements

rm(X)

remove(z2)


ls()

#installing LiblineaR package

install.packages("LiblineaR")

#Searching all installed packages


library()
search()

#Import LiblineaR


require(LiblineaR)

#removing the packages


detach("package:LiblineaR",unload = TRUE)

#or

remove.packages("LiblineaR")


#importing available iris dataset

data()


?iris

#checking structure

str(iris)

iris

data("iris")


#reading existing data


Product <- read.table("D:/Programming/python/machine learning/Machine Learning/r_language/basic_commands/Product.txt",header = TRUE,sep = "\t")

str(Product)


Customer <- read.csv("D:/Programming/python/machine learning/Machine Learning/r_language/basic_commands/Customer.csv",header = TRUE)



Customer


View(Customer)




