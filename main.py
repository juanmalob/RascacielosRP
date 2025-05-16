from flask import Flask, render_template_string, request, redirect, url_for, session

app = Flask(__name__)
# IMPORTANTE: ¡CAMBIA ESTO POR UNA CLAVE SECRETA FUERTE, ÚNICA Y ALEATORIA!
app.secret_key = 'mi_clave_secreta_super_segura_y_complicada_XYZ123!@#_v5_test'

# --- CONTENIDO HTML DE LAS PÁGINAS ---

html_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Rascacielos RP</title>
    <style>
        body {
            font-family: 'Arial', sans-serif;
            background: linear-gradient(to right, #6a0dad, #f9d423);
            margin: 0;
            padding: 0;
            color: #ffffff;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
            overflow-x: hidden;
        }
        header {
            position: relative;
            text-align: center;
            padding-bottom: 20px;
        }
        .banner {
            background-image: url('https://media.discordapp.net/attachments/1367233694737235988/1371755996896170024/BY.webp?ex=68244ad3&is=6822f953&hm=765f417c5cb35ec1b9d25128d43aac346fdada70727e823c6326a66b27f2bc20&=&format=webp&width=1251&height=626');
            background-size: cover;
            background-position: center;
            height: 250px;
            display: flex;
            align-items: center;
            justify-content: center;
            border-bottom: 3px solid #f9d423;
        }
        .banner h1 {
            margin: 0;
            font-size: 3.5em;
            text-shadow: 3px 3px 6px rgba(0, 0, 0, 0.6);
        }
        nav {
            position: absolute;
            top: 20px;
            right: 20px;
            background: rgba(0,0,0,0.6);
            padding: 12px 15px;
            border-radius: 8px;
            z-index: 1000;
        }
        nav a {
            color: #f0f0f0;
            text-decoration: none;
            margin: 0 10px; /* Ajustado */
            font-weight: bold;
            transition: color 0.3s ease;
        }
        nav a:hover {
            color: #f9d423;
        }
        .main-content {
            flex-grow: 1;
            padding-bottom: 70px;
        }
        .info-juego, .redes-sociales, .imagen-tienda-home {
            padding: 25px;
            text-align: center;
            background: rgba(0, 0, 0, 0.75);
            margin: 25px auto;
            border-radius: 10px;
            max-width: 850px;
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
            opacity: 0;
            transform: translateY(30px);
            transition: opacity 0.8s ease-out, transform 0.8s ease-out;
        }
        .info-juego.visible, .redes-sociales.visible, .imagen-tienda-home.visible {
            opacity: 1;
            transform: translateY(0);
        }
        .info-juego h2 {
            color: #f9d423;
            margin-bottom: 15px;
        }
        .redes-sociales img {
            width: 55px;
            margin: 0 15px;
            transition: transform 0.3s ease;
        }
        .redes-sociales img:hover {
            transform: scale(1.15);
        }
        .imagen-tienda-home img {
            max-width: 90%;
            height: auto;
            border-radius: 8px;
            box-shadow: 0 0 15px rgba(0,0,0,0.5);
        }
        footer {
            text-align: center;
            padding: 20px;
            background: rgba(0, 0, 0, 0.85);
            color: #cccccc;
            width: 100%;
            box-sizing: border-box;
            margin-top: auto;
        }
    </style>
</head>
<body>
    <header>
        <div class="banner">
            <h1>Rascacielos RP</h1>
        </div>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>

    <div class="main-content">
        <div class="info-juego fade-in-section">
            <h2>✨ Sobre Nosotros ✨</h2>
            <p>🎭 Rascacielos RP es un servidor de rol serio en FiveM, diseñado para ofrecer una experiencia inmersiva, realista y divertida dentro del universo de Los Santos. Nuestra misión es crear un espacio donde puedas desarrollar tu personaje y tu historia con total libertad, siempre con respeto y calidad.</p>
            <p>👥 Contamos con un Staff activo 24/7, listo para ayudarte en todo momento, resolver dudas o intervenir cuando sea necesario para mantener una comunidad sana y equilibrada.</p>
            <p>⚙️ Nuestro servidor está altamente optimizado, con scripts de última generación como los de Origne, junto a sistemas personalizados que garantizan una jugabilidad fluida, estable y llena de posibilidades.</p>
            <p>✅ El acceso se realiza mediante una whitelist sencilla y accesible, ideal tanto para jugadores nuevos como para rolers con experiencia. No necesitas ser un experto, solo tener ganas de rolear y aportar al entorno con seriedad y compromiso.</p>
            <p>🌆 Únete a Rascacielos RP y descubre una comunidad activa, organizada y en constante crecimiento, donde cada historia importa y cada personaje puede llegar hasta lo más alto.</p>
        </div>

        <div class="redes-sociales fade-in-section">
            <h3>🔗 Síguenos en Redes Sociales</h3>
            <a href="https://www.tiktok.com/@rascacielosrp.oficial" target="_blank">
                <img src="https://media.discordapp.net/attachments/1367233694737235988/1371755996615020575/images-removebg-preview.png?ex=68244ad3&is=6822f953&hm=254a030167b5d6d3cf9223168a8597c57edcfe3d31871b0cdb6f31ffc90f879b&=&format=webp&quality=lossless&width=338&height=338" alt="TikTok">
            </a>
            <a href="https://discord.gg/NbcDH5Eea4" target="_blank">
                <img src="https://media.discordapp.net/attachments/1367233694737235988/1371755996359299102/download-removebg-preview.png?ex=68244ad3&is=6822f953&hm=8d2cc547187f5d7ff3bd7e1b7861ceea45efcaf5dd98b1c6cc0befa5c3971c91&=&format=webp&quality=lossless&width=225&height=222" alt="Discord">
            </a>
        </div>

        <div class="imagen-tienda-home fade-in-section">
            <img src="https://media.discordapp.net/attachments/1367233694737235988/1371755996896170024/BY.webp?ex=68244ad3&is=6822f953&hm=765f417c5cb35ec1b9d25128d43aac346fdada70727e823c6326a66b27f2bc20&=&format=webp&width=1251&height=626" alt="Tienda Rascacielos RP">
        </div>
    </div>

    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const fadeSections = document.querySelectorAll('.fade-in-section');
            if (!fadeSections.length) return;

            const observerOptions = {
                root: null,
                rootMargin: '0px',
                threshold: 0.1
            };

            const observer = new IntersectionObserver((entries, observerInstance) => {
                entries.forEach(entry => {
                    if (entry.isIntersecting) {
                        entry.target.classList.add('visible');
                        observerInstance.unobserve(entry.target);
                    }
                });
            }, observerOptions);

            fadeSections.forEach(section => {
                observer.observe(section);
            });
        });
    </script>
</body>
</html>
"""

normativa_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Normativa - Rascacielos RP</title>
    <style>
        body {font-family: Arial, sans-serif; background: linear-gradient(to right, #6a0dad, #f9d423); margin: 0; padding: 0; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column;}
        header {position: relative; padding: 20px; text-align: center;}
        header h1 {text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);}
        nav {position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.6); padding: 12px 15px; border-radius: 8px; z-index:1000;}
        nav a {color: #f0f0f0; text-decoration: none; margin: 0 10px; font-weight: bold; transition: color 0.3s ease;}
        nav a:hover {color: #f9d423;}
        .main-content {flex-grow: 1; padding-bottom: 70px;}
        .info-juego {
            padding: 25px 35px; 
            text-align: left; 
            background: rgba(0, 0, 0, 0.82); 
            margin: 25px auto; 
            border-radius: 10px; 
            max-width: 900px; 
            box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        }
        .info-juego h2.titulo-normativa { 
            text-align: center; 
            color: #f9d423; 
            margin-bottom: 25px;
            font-size: 2.2em;
            border-bottom: 2px solid #f9d423;
            padding-bottom: 10px;
        }
        .info-juego h3.subtitulo-normativa { 
            color: #ffffff;
            text-align: center;
            margin-top: 10px;
            margin-bottom: 30px;
            font-size: 1.7em;
            font-weight: normal;
        }
        .info-juego .categoria-normas { 
            margin-bottom: 35px;
        }
        .info-juego .categoria-normas h4 { 
            color: #f9d423;
            font-size: 1.5em;
            margin-top: 0;
            margin-bottom: 18px;
            padding-bottom: 8px;
            border-bottom: 1px solid rgba(249, 212, 35, 0.5); 
        }
        .info-juego .categoria-normas ul {
            list-style: none; 
            padding-left: 0;
        }
        .info-juego .categoria-normas li {
            background-color: rgba(255, 255, 255, 0.05);
            border-left: 4px solid #f9d423;
            padding: 12px 18px;
            margin-bottom: 12px;
            border-radius: 0 5px 5px 0;
            line-height: 1.6;
            color: #e0e0e0; 
            transition: background-color 0.3s ease;
        }
        .info-juego .categoria-normas li:hover {
            background-color: rgba(255, 255, 255, 0.1);
        }
         .info-juego .categoria-normas ul ul { 
            margin-top: 8px;
            padding-left: 20px; 
        }
        .info-juego .categoria-normas ul ul li {
            background-color: rgba(255, 255, 255, 0.02); 
            border-left: 3px solid #6a0dad; 
            font-size: 0.95em;
        }
        .info-juego .norma-importante { 
            margin-top: 30px;
            padding: 18px;
            background-color: rgba(106, 13, 173, 0.3); 
            border: 1px solid #f9d423;
            border-radius: 8px;
            color: #ffffff;
            font-weight: bold;
            text-align: center;
            line-height: 1.7;
        }
        .info-juego .norma-importante strong {
            color: #f9d423;
        }
        footer {text-align: center; padding: 20px; background: rgba(0, 0, 0, 0.85); color: #cccccc; width: 100%; box-sizing: border-box; margin-top: auto;}
    </style>
</head>
<body>
    <header>
        <h1>Normativa - Rascacielos RP</h1>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>
    <div class="main-content">
        <div class="info-juego">
            <h2 class="titulo-normativa">📜 Normativa del Servidor</h2>
            <h3 class="subtitulo-normativa">Normativa General del Servidor</h3>

            <div class="categoria-normas">
                <h4>I. NORMAS GENERALES</h4>
                <ul>
                    <li><strong>Respeto:</strong> Trata a todos los jugadores y al personal con respeto. No se tolerará ningún tipo de acoso, insulto, discriminación o comportamiento tóxico.</li>
                    <li><strong>Roleplay (RP):</strong> Mantén el personaje en todo momento. Evita hablar fuera de personaje (OOC) en el juego, a menos que sea estrictamente necesario y utilizando los canales designados (/ooc).</li>
                    <li><strong>Software de Terceros:</strong> Está prohibido el uso de hacks, cheats, exploits o cualquier software que otorgue una ventaja injusta.</li>
                    <li><strong>Metagaming (MG):</strong> No utilices información obtenida fuera del juego (OOC) para beneficio de tu personaje dentro del juego (IC).</li>
                    <li><strong>Powergaming (PG):</strong> No fuerces acciones sobre otros jugadores sin darles la oportunidad de reaccionar. No realices acciones que serían imposibles en la vida real.</li>
                    <li><strong>Vehicle Deathmatch (VDM):</strong> No utilices tu vehículo como arma para atropellar intencionadamente a otros jugadores sin un motivo de rol válido.</li>
                    <li><strong>Random Deathmatch (RDM):</strong> No ataques ni mates a otros jugadores sin un motivo de rol previo y justificado.</li>
                    <li><strong>Valorar la Vida:</strong> Actúa como lo harías en la vida real si tu vida estuviera en peligro. No te pongas en situaciones de riesgo innecesarias sin motivo.</li>
                    <li><strong>No Combat Logging:</strong> No te desconectes del servidor durante una situación de rol activa, especialmente si estás en medio de un tiroteo, arresto o cualquier interacción importante.</li>
                    <li><strong>Uso del Chat OOC:</strong> Utiliza el chat OOC (/ooc) solo para asuntos que no puedan resolverse dentro del rol. No abuses de este chat ni lo uses para discutir o generar toxicidad.</li>
                    <li><strong>Publicidad:</strong> No se permite la publicidad de otros servidores, comunidades o servicios sin autorización previa del staff.</li>
                    <li><strong>Nombres de Personaje:</strong> Utiliza nombres de personaje realistas y apropiados. Evita nombres ofensivos, troll o que rompan la inmersión.</li>
                    <li><strong>Cuentas Múltiples:</strong> Generalmente no se permiten, consulta al staff si tienes una razón válida.</li>
                </ul>
            </div>

            <div class="categoria-normas">
                <h4>II. NORMAS DE ROLES ESPECÍFICOS</h4>
                <ul>
                    <li><strong>Policía (LSPD/BCSO):</strong>
                        <ul>
                            <li>Deben seguir los procedimientos policiales establecidos.</li>
                            <li>No abusar de su poder.</li>
                            <li>La corrupción debe ser roleada de forma coherente y no excesiva.</li>
                        </ul>
                    </li>
                    <li><strong>Servicios Médicos (EMS):</strong>
                        <ul>
                            <li>Priorizar la atención a los heridos.</li>
                            <li>Mantener la neutralidad en conflictos.</li>
                        </ul>
                    </li>
                    <li><strong>Mecánicos:</strong>
                        <ul>
                            <li>No inflar precios de forma desmedida.</li>
                            <li>Realizar reparaciones de forma realista.</li>
                        </ul>
                    </li>
                    <li><strong>Civiles:</strong>
                        <ul>
                            <li>Desarrollar un personaje con una historia y motivaciones.</li>
                            <li>No interferir en roles de servicios de emergencia sin justificación.</li>
                        </ul>
                    </li>
                    <li><strong>Criminales:</strong>
                        <ul>
                            <li>Los robos y actos delictivos deben tener un rol previo y coherente.</li>
                            <li>No realizar actos criminales excesivos o sin sentido que arruinen la experiencia de otros.</li>
                            <li>Los secuestros deben tener un propósito claro y no ser excesivamente largos o abusivos.</li>
                        </ul>
                    </li>
                </ul>
            </div>

            <div class="categoria-normas">
                <h4>III. NORMAS DE ZONAS SEGURAS</h4>
                <ul>
                    <li><strong>Definición:</strong> Comisarías, hospitales, garajes principales (spawn), y otras zonas designadas por el staff.</li>
                    <li><strong>Prohibiciones:</strong> En zonas seguras está prohibido iniciar actos hostiles, robos, secuestros, tiroteos o cualquier tipo de agresión.</li>
                    <li><strong>Excepciones:</strong> Se puede continuar un rol que haya comenzado fuera de la zona segura si la situación lo requiere (ej. persecución policial que termina cerca de comisaría), pero siempre valorando la vida y la lógica del rol.</li>
                </ul>
            </div>

            <div class="categoria-normas">
                <h4>IV. NORMAS DE COMUNICACIÓN</h4>
                <ul>
                    <li><strong>Discord:</strong> Utiliza los canales de Discord de forma adecuada y respetuosa. Sigue las normas específicas de cada canal.</li>
                    <li><strong>Micrófono:</strong> Es obligatorio tener un micrófono funcional y de calidad aceptable para una buena experiencia de rol.</li>
                    <li><strong>Ruidos de Fondo:</strong> Evita ruidos molestos (música alta, eco, etc.) que puedan interrumpir el rol de otros.</li>
                </ul>
            </div>

            <div class="categoria-normas">
                <h4>V. ECONOMÍA DEL SERVIDOR</h4>
                <ul>
                    <li><strong>Abuso de Bugs:</strong> No abuses de bugs o exploits económicos. Reporta cualquier error al staff.</li>
                    <li><strong>Transferencias Irreales:</strong> Evita transferencias de dinero o bienes sin un rol justificado.</li>
                </ul>
            </div>
            
            <div class="categoria-normas">
                <h4>VI. INTERACCIÓN CON EL STAFF</h4>
                <ul>
                    <li><strong>Respeto al Staff:</strong> Las decisiones del staff son finales. Si tienes una queja, utiliza los canales apropiados para reportarla de forma respetuosa.</li>
                    <li><strong>No Mentir al Staff:</strong> Sé honesto al interactuar con el staff.</li>
                    <li><strong>Reportes:</strong> Utiliza el sistema de reportes (ya sea en Discord o en el juego) para informar sobre incumplimientos de normas. Proporciona pruebas (vídeos, capturas) siempre que sea posible.</li>
                </ul>
            </div>

            <p class="norma-importante">
                <strong>El desconocimiento de estas normas no exime de su cumplimiento.</strong> El incumplimiento de cualquiera de estas reglas puede resultar en sanciones que van desde advertencias verbales hasta la expulsión permanente del servidor, dependiendo de la gravedad y reincidencia.<br>
                ¡El objetivo es crear una comunidad divertida, justa y respetuosa para todos!
            </p>

        </div>
    </div>
    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

whitelist_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Whitelist - Rascacielos RP</title>
    <style>
        body {font-family: Arial, sans-serif; background: linear-gradient(to right, #6a0dad, #f9d423); margin: 0; padding: 0; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column;}
        header {position: relative; padding: 20px; text-align: center;}
        header h1 {text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);}
        nav {position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.6); padding: 12px 15px; border-radius: 8px; z-index:1000;}
        nav a {color: #f0f0f0; text-decoration: none; margin: 0 10px; font-weight: bold; transition: color 0.3s ease;}
        nav a:hover {color: #f9d423;}
        .main-content {flex-grow: 1; padding-bottom: 70px;}
        .info-juego {padding: 25px; text-align: left; background: rgba(0, 0, 0, 0.75); margin: 25px auto; border-radius: 10px; max-width: 850px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);}
        .info-juego h2 {text-align: center; color: #f9d423; margin-bottom:15px;}
        .info-juego .formulario-link { 
            display: block;
            text-align: center;
            margin-top: 25px;
            padding: 15px;
            background-color: #f9d423;
            color: #4b0082; 
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.3em;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .info-juego .formulario-link:hover {
            background-color: #e0b814; 
            transform: scale(1.03);
        }
        footer {text-align: center; padding: 20px; background: rgba(0, 0, 0, 0.85); color: #cccccc; width: 100%; box-sizing: border-box; margin-top: auto;}
    </style>
</head>
<body>
    <header>
        <h1>Whitelist - Rascacielos RP</h1>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>
    <div class="main-content">
        <div class="info-juego">
            <h2>🔑 Proceso de Whitelist</h2>
            <p>Para unirte a nuestra comunidad exclusiva en Rascacielos RP, es necesario completar nuestro formulario de whitelist. Esto nos ayuda a mantener un ambiente de rol serio y de calidad para todos los jugadores.</p>
            <p>Por favor, lee atentamente las preguntas y responde con sinceridad. ¡Esperamos verte pronto en Los Santos!</p>
            
            <a href="https://forms.gle/ZXMtVMjeeTFTDgwR8" target="_blank" class="formulario-link">
                📋 Acceder al Formulario de Whitelist
            </a>
        </div>
    </div>
    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

postulaciones_staff_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Postulaciones Staff - Rascacielos RP</title>
    <style>
        body {font-family: Arial, sans-serif; background: linear-gradient(to right, #6a0dad, #f9d423); margin: 0; padding: 0; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column;}
        header {position: relative; padding: 20px; text-align: center;}
        header h1 {text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);}
        nav {position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.6); padding: 12px 15px; border-radius: 8px; z-index:1000;}
        nav a {color: #f0f0f0; text-decoration: none; margin: 0 10px; font-weight: bold; transition: color 0.3s ease;}
        nav a:hover {color: #f9d423;}
        .main-content {flex-grow: 1; padding-bottom: 70px;}
        .info-juego {padding: 25px; text-align: left; background: rgba(0, 0, 0, 0.75); margin: 25px auto; border-radius: 10px; max-width: 850px; box-shadow: 0 5px 15px rgba(0,0,0,0.3);}
        .info-juego h2 {text-align: center; color: #f9d423; margin-bottom:15px;}
        .info-juego .formulario-link { 
            display: block;
            text-align: center;
            margin-top: 25px;
            padding: 15px;
            background-color: #f9d423;
            color: #4b0082; 
            border-radius: 8px;
            text-decoration: none;
            font-weight: bold;
            font-size: 1.3em;
            transition: background-color 0.3s ease, transform 0.2s ease;
        }
        .info-juego .formulario-link:hover {
            background-color: #e0b814; 
            transform: scale(1.03);
        }
        footer {text-align: center; padding: 20px; background: rgba(0, 0, 0, 0.85); color: #cccccc; width: 100%; box-sizing: border-box; margin-top: auto;}
    </style>
</head>
<body>
    <header>
        <h1>Postulaciones Staff - Rascacielos RP</h1>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>
    <div class="main-content">
        <div class="info-juego">
            <h2>📝 Proceso de Postulación Staff</h2>
            <p>¿Interesado en formar parte del equipo de Staff de Rascacielos RP y ayudar a mantener y mejorar nuestra comunidad? ¡Este es tu lugar!</p>
            <p>Buscamos personas comprometidas, responsables y con ganas de aportar. Por favor, completa el siguiente formulario con la mayor sinceridad y detalle posible.</p>
            <p><em>Recuerda cambiar el enlace de abajo si tienes un formulario específico para postulaciones de staff.</em></p>
            
            <a href="https://forms.gle/ZXMtVMjeeTFTDgwR8" target="_blank" class="formulario-link"> {/* ¡CAMBIA ESTE ENLACE SI ES NECESARIO! */}
                📋 Acceder al Formulario de Postulación Staff
            </a>
        </div>
    </div>
    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

tienda_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Tienda Principal - Rascacielos RP</title>
    <style>
        body {font-family: Arial, sans-serif; background: linear-gradient(to right, #6a0dad, #f9d423); margin: 0; padding: 0; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column;}
        header {position: relative; padding: 20px; text-align: center;}
        header h1 {text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);}
        nav {position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.6); padding: 12px 15px; border-radius: 8px; z-index:1000;}
        nav a {color: #f0f0f0; text-decoration: none; margin: 0 10px; font-weight: bold; transition: color 0.3s ease;}
        nav a:hover {color: #f9d423;}
        .main-content {flex-grow: 1; padding: 20px 0 70px 0;}
        .categorias-tienda {display: flex; flex-wrap: wrap; justify-content: center; gap: 30px; padding: 20px;}
        .categoria-link {
            background: rgba(0, 0, 0, 0.7);
            border: 2px solid #f9d423;
            color: #ffffff;
            padding: 40px;
            border-radius: 10px;
            text-decoration: none;
            font-size: 1.8em;
            font-weight: bold;
            text-align: center;
            width: 300px;
            height: 150px;
            display: flex;
            align-items: center;
            justify-content: center;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .categoria-link:hover {
            transform: translateY(-10px) scale(1.05);
            box-shadow: 0 10px 20px rgba(0,0,0,0.4);
            color: #f9d423;
        }
        .tienda-titulo { text-align:center; margin-bottom: 30px; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);}
        footer {text-align: center; padding: 20px; background: rgba(0, 0, 0, 0.85); color: #cccccc; width: 100%; box-sizing: border-box; margin-top: auto;}
    </style>
</head>
<body>
    <header>
        <h1>Tienda - Rascacielos RP</h1>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>
    <div class="main-content">
        <h2 class="tienda-titulo">Explora Nuestras Categorías</h2>
        <section class="categorias-tienda">
            <a href="{{ url_for('tienda_coches') }}" class="categoria-link">🚗 Coches</a>
            <a href="{{ url_for('tienda_negocios') }}" class="categoria-link">🏢 Negocios</a>
            <a href="{{ url_for('tienda_org_criminales') }}" class="categoria-link">💀 Org. Criminales</a>
            <a href="{{ url_for('tienda_ropa_perso') }}" class="categoria-link">👕 Ropa Personalizada</a>
        </section>
    </div>
    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

sub_tienda_base_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ page_title }} - Rascacielos RP</title>
    <style>
        body {font-family: Arial, sans-serif; background: linear-gradient(to right, #6a0dad, #f9d423); margin: 0; padding: 0; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column;}
        header {position: relative; padding: 20px; text-align: center;}
        header h1 {text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);}
        nav {position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.6); padding: 12px 15px; border-radius: 8px; z-index:1000;}
        nav a {color: #f0f0f0; text-decoration: none; margin: 0 10px; font-weight: bold; transition: color 0.3s ease;}
        nav a:hover {color: #f9d423;}
        .main-content {flex-grow: 1; padding-bottom: 70px;}
        .productos {display: flex; justify-content: center; align-items: stretch; margin: 20px; flex-wrap: wrap; gap: 25px;}
        .producto {
            background: rgba(255, 255, 255, 0.12); 
            border: 1px solid #f9d423; 
            border-radius: 10px; 
            padding: 20px; 
            text-align: center; 
            transition: transform 0.3s ease, box-shadow 0.3s ease; 
            width: 300px; 
            box-sizing: border-box; 
            display: flex; 
            flex-direction: column; 
            justify-content: space-between;
        }
        .producto:hover {transform: translateY(-8px); box-shadow: 0 10px 20px rgba(0, 0, 0, 0.35);}
        
        .producto-imagen {
            width: 100%; 
            height: 180px; 
            object-fit: cover; 
            border-radius: 6px; 
            margin-bottom: 15px; 
            border: 1px solid rgba(249, 212, 35, 0.2); 
        }

        .producto .producto-info { 
            flex-grow: 1; 
            display: flex; 
            flex-direction: column;
            justify-content: center;
        }
        .producto h2 {font-size: 1.6em; margin-top: 0; margin-bottom: 10px; color: #f9d423;}
        .producto p {margin-bottom: 10px; flex-grow: 0; font-size: 0.9em; line-height: 1.5;} 
        .producto p.precio {font-weight: bold; color: #ffffff; font-size: 1.1em; margin-top:auto; margin-bottom: 15px;} 

        .producto form { margin-top: auto; }
        .producto button {background-color: #f9d423; color: #4b0082; border: none; padding: 12px 20px; border-radius: 6px; cursor: pointer; font-weight: bold; transition: background-color 0.3s ease, transform 0.2s ease; text-transform: uppercase; letter-spacing: 0.5px; width:100%;} 
        .producto button:hover {background-color: #e0b814; transform: scale(1.03);}
        
        .sub-tienda-titulo { text-align:center; margin: 30px 0; font-size: 2.5em; text-shadow: 2px 2px 4px rgba(0,0,0,0.5);}
        .volver-tienda { text-align:center; margin-bottom: 30px;}
        .volver-tienda a { color: #fff; background-color: #6a0dad; padding: 10px 20px; border-radius: 5px; text-decoration: none; font-weight: bold; transition: background-color 0.3s;}
        .volver-tienda a:hover { background-color: #5e0b99;}
        footer {text-align: center; padding: 20px; background: rgba(0, 0, 0, 0.85); color: #cccccc; width: 100%; box-sizing: border-box; margin-top: auto;}
    </style>
</head>
<body>
    <header>
        <h1>Tienda - {{ page_title }}</h1>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>
    <div class="main-content">
        <h2 class="sub-tienda-titulo">{{ page_title }}</h2>
        <div class="volver-tienda"><a href="{{ url_for('tienda') }}">← Volver a Categorías de Tienda</a></div>
        <section class="productos">
            {{ products_html|safe }}
        </section>
    </div>
    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

coches_products_html = """
    <div class="producto">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcR4Lz1hf0d20JUQ5amViujlaPxPjAx8pOp-78KUPvwghH60CC9SZw&s=10&ec=72940544" alt="Deportivo Veloz" class="producto-imagen">
        <div class="producto-info">
            <h2>Coche 15€</h2>
            <p>Un coche deportivo tuneado para alcanzar velocidades de vértigo.</p>
            <p class="precio">Precio: 15 €</p>
        </div>
        <form method="POST" action="/add_to_cart_test">
            <input type="hidden" name="producto_nombre" value="Coche 15€">
            <input type="hidden" name="producto_precio" value="15">
            <button type="submit">Añadir al Carrito</button>
        </form>
    </div>
    <div class="producto">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQGbO0hd_y2zgDCBWKtTwxGz5eFR_MquFDYlj0mtD2oNoWvY1WwZQ&s=10&ec=72940544" alt="Todoterreno Robusto" class="producto-imagen">
        <div class="producto-info">
            <h2>coche 20€</h2>
            <p>Perfecto para escapar. Imparable.</p>
            <p class="precio">Precio: 20 €</p>
        </div>
        <form method="POST" action="/add_to_cart_test">
            <input type="hidden" name="producto_nombre" value="Coche 20€">
            <input type="hidden" name="producto_precio" value="20">
            <button type="submit">Añadir al Carrito</button>
        </form>
    </div>
"""

negocios_products_html = """
    <div class="producto">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRz4f2XF5MMt3lna55c4rWjJjofg3RIJrmVg_nsp59sodWQc47Apg&s=10&ec=72940544" alt="Bar Nocturno" class="producto-imagen">
        <div class="producto-info">
            <h2>negocios</h2>
            <p>Negocio a escoger via discord.</p>
            <p class="precio">Precio: 35 €</p>
        </div>
        <form method="POST" action="/add_to_cart_test">
            <input type="hidden" name="producto_nombre" value="Negocio">
            <input type="hidden" name="producto_precio" value="35">
            <button type="submit">Añadir al Carrito</button>
        </form>
    </div>
"""

org_criminales_products_html = """
    <div class="producto">
        <img src="https://media.discordapp.net/attachments/1352002995348574294/1354162763920052254/SPOILER_image.png?ex=68258c1a&is=68243a9a&hm=f0b9b3542f10f4d7efd47bd5f87fc6cc7fc293553834bfd5eab2329595bbde1a&=&format=webp&quality=lossless&width=1112&height=626" alt="Pack Mafioso" class="producto-imagen">
        <div class="producto-info">
            <h2>Pack Mafioso🔫</h2>
            <p>Todo lo necesario para empezar tu imperio criminal: mapeado + bunker + helicoptero + lavado de dinero + meta en sede.</p>
            <p class="precio">Precio: 65 €</p>
        </div>
        <form method="POST" action="/add_to_cart_test">
            <input type="hidden" name="producto_nombre" value="Pack Mafioso">
            <input type="hidden" name="producto_precio" value="65">
            <button type="submit">Añadir al Carrito</button>
        </form>
    </div>
"""

ropa_perso_products_html = """
    <div class="producto">
        <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmcja8Jd2zFNzKEvNM-xz2Ju7_W-xWFPrwyTdIocSzhOwicsHQMw&s=10&ec=72940544" alt="Traje Exclusivo" class="producto-imagen">
        <div class="producto-info">
            <h2>Traje Exclusivo</h2>
            <p>Puede ser tu ropa perso o que te la hagamos nosotros por 7€.</p>
            <p class="precio">Precio: 5 €</p>
        </div>
        <form method="POST" action="/add_to_cart_test">
            <input type="hidden" name="producto_nombre" value="Traje Exclusivo">
            <input type="hidden" name="producto_precio" value="5">
            <button type="submit">Añadir al Carrito</button>
        </form>
    </div>
"""

carrito_content = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Carrito - Rascacielos RP</title>
    <style>
        body {font-family: Arial, sans-serif; background: linear-gradient(to right, #6a0dad, #f9d423); margin: 0; padding: 0; color: #ffffff; min-height: 100vh; display: flex; flex-direction: column;}
        header {position: relative; padding: 20px; text-align: center;}
        header h1 {text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7);}
        nav {position: absolute; top: 20px; right: 20px; background: rgba(0,0,0,0.6); padding: 12px 15px; border-radius: 8px; z-index:1000;}
        nav a {color: #f0f0f0; text-decoration: none; margin: 0 10px; font-weight: bold; transition: color 0.3s ease;}
        nav a:hover {color: #f9d423;}
        .main-content {flex-grow: 1; padding-bottom: 70px;}
        .carrito-container {padding: 30px; background: rgba(0, 0, 0, 0.8); margin: 25px auto; border-radius: 10px; max-width: 950px; box-shadow: 0 6px 18px rgba(0,0,0,0.35);}
        .carrito-container h2 {text-align: center; margin-bottom: 30px; font-size: 2.2em; color: #f9d423;}
        .cart-items {display: flex; flex-wrap: wrap; justify-content: center; gap: 25px;}
        .producto-carrito {background: rgba(255, 255, 255, 0.18); border: 1px solid #f9d423; border-radius: 10px; padding: 22px; width: 270px; box-sizing: border-box; text-align: center; transition: transform 0.3s ease, box-shadow 0.3s ease; display: flex; flex-direction: column; justify-content: space-between;}
        .producto-carrito:hover {transform: translateY(-5px); box-shadow: 0 8px 16px rgba(0,0,0,0.3);}
        .producto-carrito h3 {margin-top: 0; margin-bottom: 12px; font-size: 1.5em; color: #ffffff;}
        .producto-carrito p {margin-bottom: 18px; color: #e8e8e8; flex-grow: 1; font-size: 1em;}
        .eliminar {background: #e74c3c; color: #ffffff; border: none; padding: 12px 18px; border-radius: 6px; cursor: pointer; transition: background-color 0.3s ease, transform 0.2s ease; font-weight: bold; margin-top: auto; text-transform: uppercase; letter-spacing: 0.5px;}
        .eliminar:hover {background: #c0392b; transform: scale(1.03);}
        .empty-cart-message {text-align: center; font-size: 1.4em; margin-top: 35px; color: #f0f0f0;}
        .empty-cart-message a {color: #f9d423; text-decoration: underline; font-weight:bold;}
        .total-carrito {text-align: right; font-size: 1.6em; margin-top: 35px; padding-top: 25px; border-top: 2px solid #f9d423; color: #f9d423;}
        .total-carrito strong {color: #ffffff;}
        .paypal-button-container { text-align: right; margin-top: 25px; }
        .paypal-button {
            background-color: #ffc439; 
            color: #003087; 
            padding: 12px 25px;
            border: none;
            border-radius: 5px;
            font-size: 1.1em;
            font-weight: bold;
            cursor: pointer;
            transition: background-color 0.3s ease;
            text-decoration: none; 
            display: inline-block;
        }
        .paypal-button:hover {
            background-color: #f5b622;
        }
        .instruccion-discord {
            text-align: center;
            margin-top: 25px;
            padding: 15px;
            background-color: rgba(106, 13, 173, 0.2); 
            border: 1px dashed #f9d423;
            border-radius: 8px;
            font-size: 0.95em;
            line-height: 1.6;
            color: #f0f0f0;
        }
        .instruccion-discord strong {
            color: #ffffff;
        }
        footer {text-align: center; padding: 20px; background: rgba(0, 0, 0, 0.85); color: #cccccc; width: 100%; box-sizing: border-box; margin-top: auto;}
    </style>
</head>
<body>
    <header>
        <h1>Carrito - Rascacielos RP</h1>
        <nav>
            <a href="{{ url_for('home') }}">Inicio</a>
            <a href="{{ url_for('normativa') }}">Normativa</a>
            <a href="{{ url_for('whitelist') }}">Whitelist</a>
            <a href="{{ url_for('postulaciones_staff') }}">Postulaciones Staff</a>
            <a href="{{ url_for('tienda') }}">Tienda</a>
            <a href="{{ url_for('carrito') }}">Carrito</a>
        </nav>
    </header>
    <div class="main-content">
        <div class="carrito-container">
            <h2>🛒 Productos en tu Carrito</h2>
            {% if current_cart_items and current_cart_items|length > 0 %}
                <div class="cart-items">
                    {% set total_general = namespace(value=0) %}
                    {% for item_dict in current_cart_items %}
                        {% set total_general.value = total_general.value + item_dict.precio %}
                        <div class="producto-carrito">
                            <div>
                                <h3>{{ item_dict.nombre }}</h3>
                                <p>Precio: {{ "%.2f"|format(item_dict.precio) }} €</p>
                            </div>
                            <form method="POST" action="{{ url_for('eliminar_del_carrito_ruta') }}">
                                <input type="hidden" name="item_index" value="{{ loop.index0 }}">
                                <button type="submit" class="eliminar">Eliminar</button>
                            </form>
                        </div>
                    {% endfor %}
                </div>
                <div class="total-carrito">
                    <strong>Total: {{ "%.2f"|format(total_general.value) }} €</strong>
                </div>

                <div class="paypal-button-container">
                    <form action="https://www.paypal.com/cgi-bin/webscr" method="post" target="_top">
                        <input type="hidden" name="cmd" value="_xclick">
                        <input type="hidden" name="business" value="joan">
                        <input type="hidden" name="item_name" value="Compra en Tienda Rascacielos RP">
                        <input type="hidden" name="amount" value="{{ "%.2f"|format(total_general.value) }}">
                        <input type="hidden" name="currency_code" value="EUR">
                        <input type="hidden" name="return" value="{{ url_for('pago_exitoso', _external=True) }}">
                        <input type="hidden" name="cancel_return" value="{{ url_for('pago_cancelado', _external=True) }}">
                        <input type="hidden" name="undefined_quantity" value="0">
                        <input type="hidden" name="no_shipping" value="1">
                        <button type="submit" class="paypal-button">Pagar con PayPal</button>
                        <img alt="" border="0" src="https://www.paypalobjects.com/en_US/i/scr/pixel.gif" width="1" height="1">
                    </form>
                </div>
                
                <p class="instruccion-discord">
                    <strong>Importante:</strong> Después de completar el pago, por favor envía una captura de pantalla de tu <strong>pedido en esta página</strong> y del <strong>comprobante de pago de PayPal</strong> a nuestro canal de Discord <a href="https://discord.gg/NbcDH5Eea4" target="_blank" style="color: #f9d423;">#pedidos-tienda</a> (o el canal designado) para procesar tu compra.
                </p>

            {% else %}
                <p class="empty-cart-message">Tu carrito está vacío. ¡Visita la <a href="{{ url_for('tienda') }}">tienda</a> para añadir productos!</p>
            {% endif %}
        </div>
    </div>
    <footer>
        <p>© 2025 Rascacielos RP. Todos los derechos reservados.</p>
    </footer>
</body>
</html>
"""

# --- LÓGICA DE LAS RUTAS FLASK ---

@app.route('/')
def home():
    return render_template_string(html_content)

@app.route('/normativa')
def normativa():
    return render_template_string(normativa_content)

@app.route('/whitelist')
def whitelist():
    return render_template_string(whitelist_content)

@app.route('/postulaciones_staff') # RUTA NUEVA
def postulaciones_staff():
    return render_template_string(postulaciones_staff_content)

@app.route('/tienda')
def tienda():
    return render_template_string(tienda_content)

@app.route('/tienda/coches')
def tienda_coches():
    return render_template_string(sub_tienda_base_content, page_title="Coches", products_html=coches_products_html)

@app.route('/tienda/negocios')
def tienda_negocios():
    return render_template_string(sub_tienda_base_content, page_title="Negocios", products_html=negocios_products_html)

@app.route('/tienda/org_criminales')
def tienda_org_criminales():
    return render_template_string(sub_tienda_base_content, page_title="Organizaciones Criminales", products_html=org_criminales_products_html)

@app.route('/tienda/ropa_perso')
def tienda_ropa_perso():
    return render_template_string(sub_tienda_base_content, page_title="Ropa Personalizada", products_html=ropa_perso_products_html)

@app.route('/add_to_cart_test', methods=['POST'])
def add_to_cart_test_route():
    nombre_producto = request.form.get('producto_nombre')
    precio_producto_str = request.form.get('producto_precio')
    cart_items = session.get('cart', [])

    if nombre_producto and precio_producto_str:
        try:
            precio_producto = float(precio_producto_str)
            # Corrección para asegurar que el precio del formulario se usa si está presente
            # Si el nombre del producto ya implica un precio (ej. "Coche 15€"), podrías
            # extraerlo del nombre, pero es más robusto tomarlo del campo 'producto_precio'
            cart_items.append({'nombre': nombre_producto, 'precio': precio_producto})
            session['cart'] = cart_items
            session.modified = True
        except ValueError:
            pass 
    return redirect(url_for('carrito'))


@app.route('/carrito', methods=['GET'])
def carrito():
    current_cart_items = session.get('cart', [])
    return render_template_string(carrito_content, current_cart_items=current_cart_items)


@app.route('/eliminar_del_carrito', methods=['POST'])
def eliminar_del_carrito_ruta():
    cart_items = session.get('cart', [])
    try:
        item_index_str = request.form.get('item_index')
        if item_index_str is not None:
            item_index = int(item_index_str)
            if 0 <= item_index < len(cart_items):
                cart_items.pop(item_index)
                session['cart'] = cart_items
                session.modified = True
    except ValueError:
        pass 
    return redirect(url_for('carrito'))

@app.route('/pago_exitoso')
def pago_exitoso():
    session.pop('cart', None) 
    session.modified = True
    mensaje_exito = """
    <!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Pago Exitoso</title>
    <style>body{font-family:Arial,sans-serif;background:linear-gradient(to right, #6a0dad, #f9d423);color:white;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;text-align:center;} .container{background:rgba(0,0,0,0.7);padding:40px;border-radius:10px;}</style></head>
    <body><div class="container"><h1>¡Gracias por tu compra!</h1><p>Tu pago ha sido procesado (esto es una simulación, el carrito se ha vaciado).</p><p>Recuerda enviar las capturas a nuestro Discord como se indicó.</p><p><a href="{}" style="color:#f9d423;">Volver a la tienda</a></p></div></body></html>
    """.format(url_for('tienda'))
    return render_template_string(mensaje_exito)

@app.route('/pago_cancelado')
def pago_cancelado():
    mensaje_cancelado = """
    <!DOCTYPE html><html lang="es"><head><meta charset="UTF-8"><title>Pago Cancelado</title>
    <style>body{font-family:Arial,sans-serif;background:linear-gradient(to right, #6a0dad, #f9d423);color:white;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;text-align:center;} .container{background:rgba(0,0,0,0.7);padding:40px;border-radius:10px;}</style></head>
    <body><div class="container"><h1>Pago Cancelado</h1><p>Has cancelado el proceso de pago. Tu carrito sigue intacto.</p><p><a href="{}" style="color:#f9d423;">Volver al carrito</a></p><p><a href="{}" style="color:#f9d423;">Volver a la tienda</a></p></div></body></html>
    """.format(url_for('carrito'), url_for('tienda'))
    return render_template_string(mensaje_cancelado)


if __name__ == '__main__':
    app.run(debug=True, port=5000)