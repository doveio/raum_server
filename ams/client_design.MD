```
from ams import connection
```

```
con = connection.Connect()
```

```
con.Project.create()
myproject = con.Project.get(code='demo')
```
```
con.Asset.create(project=myproject,
                code='simba',
                asset_type='char',
                frame_range = {
                    'cut_in': 1001,
                    'cut_out: 1002
                })
myasset = con.Asset.get(project=myproject, code='simba)

myasset.client_name = 'Simba Child'
myasset.save()

myasset.add_chidlren(asset_list = [])
myasset.add_variant(asset_list = [])

myasset.get_chidlren()
myasset.get_variant()
```

```
con.Bundle.create('project', 'asset', 'process', 'element')
con.Bundle.get('project', 'asset', 'process', 'element', status='approved')
con.Bundle.get('project', 'asset', 'process', 'element')
con.Bundle.set_status('approved')
```

```
con.Product.create('bundle', 'data_type', 'filepath', 'extension')

myproduct = con.Product.get('bundle', 'data_type', 'filepath', 'extension')
product_from_patht = con.Product.get_from_path(filepath)

myyprooduct.add_dependencies(products=[])
```