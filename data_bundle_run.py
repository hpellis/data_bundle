from data_bundle import data_bundle_purchase


result = data_bundle_purchase('1234', 34.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 2')
result = data_bundle_purchase('2345', -22.00)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

print ('TEST EXAMPLE 3')
result = data_bundle_purchase('3456', 17.55)
print ('-----\nRESULT:', result)
print ('-' * 50, '\n')

