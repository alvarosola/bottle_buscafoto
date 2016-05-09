<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns ="http://www.w3.org/1999/xhtml" xml:lang="es">
	<head>
		<title>Busca fotos</title>
		<!-- Bootstrap core CSS -->
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css" rel="stylesheet">
        <link href="//netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css" rel="stylesheet">
        <link href="//netdna.bootstrapcdn.com/font-awesome/4.0.3/css/font-awesome.min.css" rel="stylesheet">	
		<link href="/static/estilo.css" rel="stylesheet">
		<img class="fondo" src="/static/fondo.png" alt="">
	</head>
	<body>
		<h1>Busca fotos</h1>
		<form action = '/busqueda' method='POST'>
			<h2>Bienvenido, introduzca el nombre de foto que quiera ver.</h2>
			<input type = 'text' name='foto' size='50' placeholder='Introduzca un nombre'/>
			<input type = 'submit' value='Buscar' class="btn btn-success" />
		</form>
	</body>
</html>

