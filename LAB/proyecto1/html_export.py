from datetime import datetime


def export_recipe(c_n, add, nit, tip, items, sub, tot, invoices):
    element_table = ""

    for el in items:
        element_table += f'<tr class="details"><td>({el[0]}) {el[1]}</td><td>Q{el[2]}</td></tr>'

    now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    finalstring = f'<!DOCTYPE html> <html> 	<head> 		<meta charset="utf-8" /> 		<title>Factura LFP</title>  		<style> 			.invoice-box {{ 				max-width: 800px; 				margin: auto; 				padding: 30px; 				border: 1px solid #eee; 				box-shadow: 0 0 10px rgba(0, 0, 0, 0.15); 				font-size: 16px; 				line-height: 24px; 				font-family: "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; 				color: #555; 			}}  			.invoice-box table {{ 				width: 100%; 				line-height: inherit; 				text-align: left; 			}}  			.invoice-box table td {{ 				padding: 5px; 				vertical-align: top; 			}}  			.invoice-box table tr td:nth-child(2) {{ 				text-align: right; 			}}  			.invoice-box table tr.top table td {{ 				padding-bottom: 20px; 			}}  			.invoice-box table tr.top table td.title {{ 				font-size: 45px; 				line-height: 45px; 				color: #333; 			}}  			.invoice-box table tr.information table td {{ 				padding-bottom: 40px; 			}}  			.invoice-box table tr.heading td {{ 				background: #eee; 				border-bottom: 1px solid #ddd; 				font-weight: bold; 			}}  			.invoice-box table tr.details td {{ 				padding-bottom: 20px; 			}}  			.invoice-box table tr.item td {{ 				border-bottom: 1px solid #eee; 			}}  			.invoice-box table tr.item.last td {{ 				border-bottom: none; 			}}  			.invoice-box table tr.total td:nth-child(2) {{ 				border-top: 2px solid #eee; 				font-weight: bold; 			}}  			@media only screen and (max-width: 600px) {{ 				.invoice-box table tr.top table td {{ 					width: 100%; 					display: block; 					text-align: center; 				}}  				.invoice-box table tr.information table td {{ 					width: 100%; 					display: block; 					text-align: center; 				}} 			}}  			/** RTL **/ 			.rtl {{ 				direction: rtl; 				font-family: Tahoma, "Helvetica Neue", "Helvetica", Helvetica, Arial, sans-serif; 			}}  			.rtl table {{ 				text-align: right; 			}}  			.rtl table tr td:nth-child(2) {{ 				text-align: left; 			}} 		</style> 	</head>  	<body> 		<div class="invoice-box"> 			<table cellpadding="0" cellspacing="0"> 				<tr class="top"> 					<td colspan="2"> 						<table> 							<tr> 								<td class="title"> 									<h3>LFP_P1</h3> 								</td>  								<td> 									Factura #: {invoices}<br /> 									Fecha: {now}<br /> 								</td> 							</tr> 						</table> 					</td> 				</tr>  				<tr class="information"> 					<td colspan="2"> 						<table> 							<tr> 								<td> 									LFP<br /> 									Proyecto 1<br /> 									Brian Matus, 201801290 								</td>  								<td> 									{c_n}<br /> 									{add}<br /> 									{nit} 								</td> 							</tr> 						</table> 					</td> 				</tr>  				<tr class="heading"> 					<td>Descripcion</td>  					<td>Precio</td> 				</tr>  				{element_table}     				<tr class="heading"> 					<td>Subtotal</td>  					<td>Q{sub}</td> 				</tr>  				<tr class="item"> 					<td>Propina</td>  					<td>{tip}%</td> 				</tr>  				<tr class="heading"> 					<td>Total</td>  					<td>Q{tot}</td> 				</tr>  			</table> 		</div> 	</body> </html> '
    print(finalstring)
    with open("factura_" + str(invoices) + ".html", "a", encoding="utf-8") as file:
        file.write(finalstring)
        file.close()


def export_menu(restaurant):
    menu_table = ""

    for c in restaurant.categories:
        menu_table += f'<div class="title"><h3>Menu, <span>{c.name}</span></h3></div>'
        for p in c.elements:
            #print(f'id:{p.name} name:{p.real_name} price:{p.price} description:{p.description}')

            menu_table += f'<li><div class="item"><div class="item-title"><h2>{p.real_name}</h2><div class="border-bottom"></div><span>Q{p.price}</span></div><p>{p.description}</p></div></li>'


    finalstring = f'<!DOCTYPE html> <html class="no-js"> 	<head> 		<meta charset="utf-8"> 		<title>Menu LFP</title> 		<link rel="stylesheet" href="css/bootstrap.min.css"> 		<link rel="stylesheet" href="css/font-awesome.min.css"> 		<link rel="stylesheet" href="css/main.css"> 	</head> 	<body>     <section id="price">         <div class="container">             <div class="row">                 <div class="col-md-12">                     <div class="block">                         <h1 class="heading wow fadeInUp"   data-wow-delay="300ms">Menu <span>El Mejor</span> restaurante <span>LFP</span></h1>                         <p     data-wow-delay="400ms">Bienvenidos a nuestro hermoso restaurante, echen un vistazo al menu </p>                         <div class="pricing-list">                                                          <ul>                                 {menu_table}                             </ul>                         </div>                     </div>                 </div>             </div>         </div>     </section>     <footer id="footer-bottom">         <div class="container">             <div class="row">                 <div class="col-md-12 col-sm-12">                     <div class="block">                         <p>LFP <a>Proyecto 1</a></p>                     </div>                 </div>             </div>         </div>     </footer> 	</body> </html>0'
    print(finalstring)
    with open("menu/menu.html", "a", encoding="utf-8") as file:
        file.write(finalstring)
        file.close()

