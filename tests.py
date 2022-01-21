from hello import app
with app.test_client() as c:
    response = c.get('/')
    assert b'<h1>Hello Human!</h1>' in response.data
    assert response.status_code == 200
    
    name = 'Bobblebat'
    response = c.get(f'/hello/{name}')
    # note bytes objects don't have format method but % works
    assert b'<h1>Hello %b!</h1>' % bytes(name, 'utf-8') in response.data
    assert response.status_code == 200

