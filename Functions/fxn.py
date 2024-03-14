# def greet():
#     print('hey koshy')
    
    
# greet()
#passing parameters in functions


# def hi(name):
#     print('hi '+name)
    
# hi('koshy')

#can pass parameter when defining function
def hi(name = 'koshy'):
    print('my name is '+ name)
    
hi('comfort') #this will give the defined name (comfort)
hi() #should give the default (koshy)