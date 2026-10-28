import re
import os

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Make sure footer isn't already present
if '<footer' in html:
    print('Footer already present in index.html, removing old footer first...')
    html = re.sub(r'<!-- =* FASE 9.*?</footer>', '', html, flags=re.DOTALL)
    html = re.sub(r'<footer.*?</footer>', '', html, flags=re.DOTALL)

main_end = '</main>'
idx_main_end = html.find(main_end)
if idx_main_end == -1:
    raise Exception("</main> not found in index.html")
idx_insert = idx_main_end + len(main_end)

footer_html = '''

  <!-- =======================================================================
       FASE 9 — FOOTER ISTITUZIONALE | A.S. TOP CLEAN
       Layout di chiusura premium 100% fedele al mockup originale:
       - Sfondo antracite profondo (#04070A) coordinato con header e sezioni scure
       - Barra principale:
         * Sinistra: Logo ufficiale A.S. TOP CLEAN (Detailing & Car Care)
         * Centro: Navigazione secondaria (Home, Servizi, Lavori Eseguiti, Chi Siamo, Perché Sceglierci, FAQ, Contatti)
         * Destra: Pulsante CTA coordinato "Contattaci" con icona WhatsApp e freccia
       - Linea divisoria sottile (1px solid rgba(255, 255, 255, 0.08))
       - Barra inferiore:
         * Sinistra: Copyright con anno dinamico (© [anno] A.S. TOP CLEAN. Tutti i diritti riservati.)
         * Destra: Link legali Privacy Policy e Cookie Policy
       ======================================================================= -->
  <footer class="site-footer" role="contentinfo">
    <div class="footer-container">
      
      <!-- AREA SUPERIORE ISTITUZIONALE (LOGO, NAVIGAZIONE, CTA) -->
      <div class="footer-main">
        <!-- Logo Ufficiale A.S. Top Clean -->
        <a href="#home" class="footer-logo-link" aria-label="A.S. Top Clean - Torna alla Home">
          <img src="assets/logo.svg" 
               alt="A.S. Top Clean - Detailing &amp; Car Care" 
               class="footer-logo" 
               width="168" 
               height="49" 
               loading="lazy">
        </a>

        <!-- Testo descrittivo per SEO e Screen Reader (accessibilità completa) -->
        <p class="sr-only">Ci prendiamo cura della tua auto con servizi professionali di detailing, trattamenti dedicati e attenzione ai dettagli.</p>

        <!-- Navigazione Footer: Link alle sezioni interne del sito -->
        <nav class="footer-nav" aria-label="Navigazione footer">
          <ul class="footer-nav-list">
            <li class="footer-nav-item">
              <a href="#home" class="footer-nav-link active">Home</a>
            </li>
            <li class="footer-nav-item">
              <a href="#servizi" class="footer-nav-link">Servizi</a>
            </li>
            <li class="footer-nav-item">
              <a href="#lavori" class="footer-nav-link">Lavori Eseguiti</a>
            </li>
            <li class="footer-nav-item">
              <a href="#chi-siamo" class="footer-nav-link">Chi Siamo</a>
            </li>
            <li class="footer-nav-item">
              <a href="#perche-sceglierci" class="footer-nav-link">Perché Sceglierci</a>
            </li>
            <li class="footer-nav-item">
              <a href="#faq" class="footer-nav-link">FAQ</a>
            </li>
            <li class="footer-nav-item">
              <a href="#contatti" class="footer-nav-link">Contatti</a>
            </li>
          </ul>
        </nav>

        <!-- Pulsante Contattaci (Oro, coordinato con pulsante header e WhatsApp) -->
        <div class="footer-actions">
          <a href="#contatti" class="btn-contact btn-footer-contact" id="footerContactBtn" aria-label="Contattaci su WhatsApp">
            <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true" focusable="false">
              <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.16 12.04 20.16C10.66 20.16 9.3 19.8 8.11 19.1L7.83 18.93L4.71 19.75L5.54 16.71L5.35 16.41C4.55 15.13 4.13 13.54 4.13 11.91C4.13 7.37 7.82 3.67 12.05 3.67ZM8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.7C7.02 10.92 7.91 12.1 8.03 12.26C8.16 12.43 9.77 14.91 12.23 15.97C12.82 16.22 13.27 16.37 13.63 16.49C14.22 16.67 14.76 16.65 15.19 16.59C15.67 16.51 16.66 15.98 16.87 15.4C17.07 14.81 17.07 14.31 17.01 14.21C16.95 14.11 16.79 14.05 16.54 13.92C16.29 13.8 15.08 13.21 14.85 13.13C14.63 13.04 14.46 13 14.3 13.25C14.13 13.49 13.66 14.05 13.52 14.21C13.38 14.38 13.23 14.4 12.99 14.28C12.74 14.16 11.94 13.9 10.99 13.06C10.25 12.4 9.75 11.59 9.61 11.34C9.46 11.1 9.59 10.96 9.72 10.84C9.83 10.73 9.97 10.55 10.09 10.41C10.22 10.27 10.26 10.16 10.34 10C10.42 9.84 10.38 9.7 10.32 9.58C10.26 9.46 9.77 8.25 9.57 7.76C9.37 7.29 9.17 7.35 9.02 7.34C8.87 7.33 8.71 7.33 8.53 7.33Z"/>
            </svg>
            <span class="btn-text">Contattaci</span>
            <svg class="btn-arrow" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
              <line x1="5" y1="12" x2="19" y2="12"></line>
              <polyline points="12 5 19 12 12 19"></polyline>
            </svg>
          </a>
        </div>
      </div>

      <!-- LINEA DIVISORIA SOTTILE -->
      <div class="footer-divider" aria-hidden="true"></div>

      <!-- BARRA INFERIORE: COPYRIGHT DINAMICO E LINK LEGALI -->
      <div class="footer-bottom">
        <p class="footer-copyright">
          &copy; <span id="currentYear">2026</span> A.S. TOP CLEAN. Tutti i diritti riservati.
        </p>
        <div class="footer-legal-links">
          <a href="#privacy" class="footer-legal-link">Privacy Policy</a>
          <span class="legal-separator" aria-hidden="true">|</span>
          <a href="#cookies" class="footer-legal-link">Cookie Policy</a>
        </div>
      </div>

    </div>
  </footer>'''

html = html[:idx_insert] + footer_html + html[idx_insert:]

# Bump cache-busting version
html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=9.0', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=9.0', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html successfully updated with footer!')


# 2. Update css/style.css
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure old footer css is removed if already added
if '.site-footer' in css:
    print('Removing old footer css from css/style.css...')
    css = re.sub(r'/\* =+ *\n *12\. FOOTER ISTITUZIONALE.*?(?=/\* --------------------------------------------------------------------------\n *12\. RESPONSIVE DESIGN GLOBALE)', '', css, flags=re.DOTALL)
    # Also clean responsive overrides if any
    css = re.sub(r'/\* Footer a 1280px \*/.*?\.footer-grid \{[^}]*\}', '', css, flags=re.DOTALL)
    css = re.sub(r'/\* Footer su Tablet \(1024px\) \*/.*?\.footer-grid \{[^}]*\}', '', css, flags=re.DOTALL)
    css = re.sub(r'/\* Footer su Mobile \(767px\) \*/.*?\.footer-bottom-bar \{[^}]*\}', '', css, flags=re.DOTALL)
    css = re.sub(r'/\* Footer su smartphone compatti \(480px\) \*/.*?\.footer-link \{[^}]*\}', '', css, flags=re.DOTALL)
    css = re.sub(r'/\* Footer su smartphone molto piccoli \(360px\) \*/.*?\.footer-container \{[^}]*\}', '', css, flags=re.DOTALL)

resp_marker = '/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN GLOBALE'
resp_idx = css.find(resp_marker)
if resp_idx == -1:
    raise Exception("Responsive design global marker not found in style.css")

base_footer_css = '''/* ==========================================================================
   12. FOOTER ISTITUZIONALE (.site-footer)
   - Layout ultra-premium perfettamente sincronizzato con l'header del mockup
   - Sfondo antracite profondo (#04070A) con contrasto tipografico bilanciato
   - Barra superiore flex: Logo a sinistra, Navigazione centrale, Pulsante CTA a destra
   - Linea divisoria sottile (1px solid rgba(255, 255, 255, 0.08))
   - Barra inferiore: Copyright dinamico e collegamenti Privacy & Cookie Policy
   ========================================================================== */

.site-footer {
  position: relative;
  width: 100%;
  background-color: #04070A;
  color: #94A3B8;
  padding: 44px 0 32px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.footer-container {
  width: 100%;
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 40px;
}

.footer-main {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 32px;
  gap: 32px;
}

.footer-logo-link {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
  flex-shrink: 0;
  transition: opacity var(--transition-fast);
}

.footer-logo-link:hover {
  opacity: 0.88;
}

.footer-logo {
  height: 42px;
  width: auto;
  display: block;
}

/* Navigazione centrale */
.footer-nav {
  display: flex;
  align-items: center;
  justify-content: center;
  flex: 1;
}

.footer-nav-list {
  display: flex;
  align-items: center;
  justify-content: center;
  flex-wrap: wrap;
  gap: 22px 30px;
  list-style: none;
  padding: 0;
  margin: 0;
}

.footer-nav-item {
  display: inline-flex;
  align-items: center;
}

.footer-nav-link {
  font-family: var(--font-primary);
  font-size: 13.5px;
  font-weight: 500;
  color: #94A3B8;
  text-decoration: none;
  position: relative;
  transition: color var(--transition-fast);
  padding: 4px 0;
}

.footer-nav-link:hover {
  color: var(--color-gold);
}

.footer-nav-link.active {
  color: var(--color-gold);
}

.footer-nav-link:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 4px;
  border-radius: 2px;
}

/* Pulsante CTA Destra */
.footer-actions {
  flex-shrink: 0;
  display: flex;
  align-items: center;
}

.btn-footer-contact {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 20px;
  background-color: var(--color-gold);
  color: #0D151C;
  border-radius: 9999px;
  font-family: var(--font-primary);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
  box-shadow: 0 2px 10px rgba(245, 195, 66, 0.25);
  cursor: pointer;
  border: none;
}

.btn-footer-contact:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
  box-shadow: 0 4px 14px rgba(245, 195, 66, 0.38);
  color: #0D151C;
}

.btn-footer-contact:focus-visible {
  outline: 2px solid #FFFFFF;
  outline-offset: 3px;
}

/* Linea divisoria */
.footer-divider {
  width: 100%;
  height: 1px;
  background-color: rgba(255, 255, 255, 0.08);
  margin: 0 0 24px 0;
}

/* Barra inferiore */
.footer-bottom {
  display: flex;
  align-items: center;
  justify-content: space-between;
  flex-wrap: wrap;
  gap: 14px;
  font-family: var(--font-primary);
  font-size: 12.5px;
  color: #64748B;
}

.footer-copyright {
  margin: 0;
  color: #64748B;
}

.footer-legal-links {
  display: flex;
  align-items: center;
  gap: 12px;
}

.footer-legal-link {
  color: #64748B;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-legal-link:hover {
  color: var(--color-gold);
}

.footer-legal-link:focus-visible {
  outline: 1px solid var(--color-gold);
  outline-offset: 2px;
}

.legal-separator {
  color: #334155;
  font-size: 11px;
}

'''

css = css[:resp_idx] + base_footer_css + css[resp_idx:]

# Responsive media query additions
# 1. 1280px
css = css.replace(
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }',
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }\n\n  /* Footer a 1280px */\n  .footer-container {\n    padding: 0 32px;\n  }\n\n  .footer-nav-list {\n    gap: 18px 24px;\n  }'
)

# 2. 1024px
css = css.replace(
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }',
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }\n\n  /* Footer su Tablet (1024px) */\n  .footer-container {\n    padding: 0 24px;\n  }\n\n  .footer-main {\n    flex-direction: column;\n    align-items: center;\n    text-align: center;\n    gap: 22px;\n    padding-bottom: 26px;\n  }\n\n  .footer-nav {\n    width: 100%;\n  }\n\n  .footer-nav-list {\n    justify-content: center;\n    gap: 14px 22px;\n  }'
)

# 3. 767px
css = css.replace(
    '  .contact-social-icons {\n    display: flex;\n    align-items: center;\n    justify-content: flex-start;\n    gap: 10px;\n  }\n}',
    '  .contact-social-icons {\n    display: flex;\n    align-items: center;\n    justify-content: flex-start;\n    gap: 10px;\n  }\n\n  /* Footer su Mobile (767px) */\n  .site-footer {\n    padding: 38px 0 26px 0;\n  }\n\n  .footer-container {\n    padding: 0 16px;\n  }\n\n  .footer-main {\n    flex-direction: column;\n    align-items: center;\n    text-align: center;\n    gap: 22px;\n    padding-bottom: 24px;\n  }\n\n  .footer-logo {\n    height: 38px;\n  }\n\n  .footer-nav-list {\n    flex-direction: column;\n    gap: 12px;\n    width: 100%;\n  }\n\n  .footer-nav-link {\n    display: block;\n    font-size: 14px;\n    padding: 6px 0;\n  }\n\n  .footer-actions {\n    width: 100%;\n    display: flex;\n    justify-content: center;\n  }\n\n  .btn-footer-contact {\n    width: 100%;\n    max-width: 280px;\n    padding: 11px 20px;\n    font-size: 13.5px;\n  }\n\n  .footer-bottom {\n    flex-direction: column;\n    align-items: center;\n    text-align: center;\n    gap: 10px;\n  }\n}'
)

# 4. 480px
css = css.replace(
    '/* Contatti su smartphone compatti (480px) */\n  .contact-section {\n    padding: 40px 0 46px 0;\n  }\n\n  .contact-heading {\n    font-size: 20px;\n  }\n\n  .contact-input {\n    padding: 8.5px 11px;\n    font-size: 12.5px;\n  }',
    '/* Contatti su smartphone compatti (480px) */\n  .contact-section {\n    padding: 40px 0 46px 0;\n  }\n\n  .contact-heading {\n    font-size: 20px;\n  }\n\n  .contact-input {\n    padding: 8.5px 11px;\n    font-size: 12.5px;\n  }\n\n  /* Footer su smartphone compatti (480px) */\n  .footer-copyright {\n    font-size: 12px;\n  }\n\n  .footer-legal-link {\n    font-size: 12px;\n  }'
)

# 5. 360px
css = css.replace(
    '/* Contatti su smartphone molto piccoli (360px) */\n  .contact-section {\n    padding: 34px 0 40px 0;\n  }\n\n  .contact-container {\n    padding: 0 12px;\n  }\n\n  .contact-heading {\n    font-size: 19px;\n  }\n\n  .btn-contact-whatsapp {\n    font-size: 13px;\n    padding: 10px 16px;\n  }',
    '/* Contatti su smartphone molto piccoli (360px) */\n  .contact-section {\n    padding: 34px 0 40px 0;\n  }\n\n  .contact-container {\n    padding: 0 12px;\n  }\n\n  .contact-heading {\n    font-size: 19px;\n  }\n\n  .btn-contact-whatsapp {\n    font-size: 13px;\n    padding: 10px 16px;\n  }\n\n  /* Footer su smartphone molto piccoli (360px) */\n  .footer-container {\n    padding: 0 12px;\n  }'
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css successfully updated with footer!')


# 3. Update js/main.js
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure initFooterYear is registered in DOMContentLoaded
if 'initFooterYear();' not in js:
    js = js.replace('initContactWhatsApp();', 'initContactWhatsApp();\n  initFooterYear();')

# Append helper function if not present
if 'function initFooterYear()' not in js:
    footer_js = '''
/**
 * Inizializza l'aggiornamento automatico dell'anno corrente nel footer
 */
function initFooterYear() {
  const currentYearEl = document.getElementById('currentYear');
  if (currentYearEl) {
    currentYearEl.textContent = new Date().getFullYear();
  }
}
'''
    js += footer_js

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('js/main.js successfully updated with footer!')

