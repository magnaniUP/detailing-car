import re

# 1. Update index.html to add <footer> right after </main>
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

main_end = '</main>'
idx_main_end = html.find(main_end) + len(main_end)

footer_html = '''

  <!-- =======================================================================
       FASE 9 — FOOTER ISTITUZIONALE
       Layout responsive su sfondo scuro antracite con accenti oro:
       - Colonna 1: Identità aziendale (Logo ufficiale A.S. Top Clean, Detailing & Car Care e descrizione)
       - Colonna 2: Navigazione interna (Link rapidi verso le 7 sezioni)
       - Colonna 3: I nostri servizi (Collegamenti diretti ai trattamenti di detailing)
       - Colonna 4: Contattaci (CTA WhatsApp, recapiti telefonici ed email, social)
       - Barra inferiore: Copyright con anno dinamico e link legali
       ======================================================================= -->
  <footer class="site-footer" role="contentinfo">
    <div class="footer-container">
      <div class="footer-grid">

        <!-- COLONNA 1: IDENTITÀ AZIENDALE -->
        <div class="footer-col footer-col-brand">
          <a href="#home" class="footer-logo-link" aria-label="A.S. Top Clean - Torna all'inizio della pagina">
            <img src="assets/logo.svg" 
                 alt="Logo A.S. Top Clean Detailing & Car Care" 
                 class="footer-logo" 
                 width="170" 
                 height="48" 
                 loading="lazy">
          </a>
          <p class="footer-brand-desc">
            Ci prendiamo cura della tua auto con servizi professionali di detailing, trattamenti dedicati e attenzione ai dettagli.
          </p>
          <div class="footer-social-wrap">
            <span class="footer-social-title">Seguici sui social</span>
            <div class="footer-social-links">
              <a href="https://instagram.com" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="Seguici su Instagram">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <rect x="2" y="2" width="20" height="20" rx="5" ry="5"></rect>
                  <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z"></path>
                  <line x1="17.5" y1="6.5" x2="17.51" y2="6.5"></line>
                </svg>
              </a>
              <a href="https://facebook.com" target="_blank" rel="noopener noreferrer" class="footer-social-btn" aria-label="Seguici su Facebook">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z"></path>
                </svg>
              </a>
            </div>
          </div>
        </div>

        <!-- COLONNA 2: NAVIGAZIONE (LINK RAPIDI) -->
        <div class="footer-col footer-col-nav">
          <h3 class="footer-heading">Link rapidi</h3>
          <ul class="footer-list">
            <li><a href="#home" class="footer-link">Home</a></li>
            <li><a href="#servizi" class="footer-link">Servizi</a></li>
            <li><a href="#lavori" class="footer-link">Lavori eseguiti</a></li>
            <li><a href="#chi-siamo" class="footer-link">Chi siamo</a></li>
            <li><a href="#perche-sceglierci" class="footer-link">Perché sceglierci</a></li>
            <li><a href="#faq" class="footer-link">FAQ</a></li>
            <li><a href="#contatti" class="footer-link">Contatti</a></li>
          </ul>
        </div>

        <!-- COLONNA 3: I NOSTRI SERVIZI -->
        <div class="footer-col footer-col-services">
          <h3 class="footer-heading">I nostri servizi</h3>
          <ul class="footer-list">
            <li><a href="#servizi" class="footer-link">Lavaggio Detailing</a></li>
            <li><a href="#servizi" class="footer-link">Protezione Ceramica</a></li>
            <li><a href="#servizi" class="footer-link">Trattamento Interni</a></li>
            <li><a href="#servizi" class="footer-link">Lucidatura e Correzione</a></li>
            <li><a href="#servizi" class="footer-link">Restauro Fari</a></li>
            <li><a href="#servizi" class="footer-link">Sanificazione Auto</a></li>
          </ul>
        </div>

        <!-- COLONNA 4: CONTATTACI -->
        <div class="footer-col footer-col-contact">
          <h3 class="footer-heading">Contattaci</h3>
          
          <div class="footer-contact-items">
            <a href="tel:+393911234567" class="footer-contact-item" aria-label="Telefono: +39 391 123 4567">
              <span class="footer-contact-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path>
                </svg>
              </span>
              <span>+39 391 123 4567</span>
            </a>

            <a href="mailto:info@astopclean.it" class="footer-contact-item" aria-label="Email: info@astopclean.it">
              <span class="footer-contact-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"></path>
                  <polyline points="22,6 12,13 2,6"></polyline>
                </svg>
              </span>
              <span>info@astopclean.it</span>
            </a>

            <div class="footer-contact-item footer-address-item">
              <span class="footer-contact-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="16" height="16" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                  <path d="M21 10c0 7-9 13-9 13s-9-6-9-13a9 9 0 0 1 18 0z"></path>
                  <circle cx="12" cy="10" r="3"></circle>
                </svg>
              </span>
              <span>Via Roma 123, Milano, Italia</span>
            </div>
          </div>

          <div class="footer-cta-wrap">
            <a href="https://wa.me/393911234567?text=Buongiorno%20A.S.%20Top%20Clean!%20Vorrei%20maggiori%20informazioni%20sui%20vostri%20servizi." 
               class="btn-footer-whatsapp" 
               target="_blank" 
               rel="noopener noreferrer" 
               aria-label="Contattaci su WhatsApp">
              <span class="btn-wa-icon" aria-hidden="true">
                <svg viewBox="0 0 24 24" width="18" height="18" fill="currentColor">
                  <path d="M17.472 14.382c-.297-.149-1.758-.867-2.03-.967-.273-.099-.471-.148-.67.15-.197.297-.767.966-.94 1.164-.173.199-.347.223-.644.075-.297-.15-1.255-.463-2.39-1.475-.883-.788-1.48-1.761-1.653-2.059-.173-.297-.018-.458.13-.606.134-.133.298-.347.446-.52.149-.174.198-.298.298-.497.099-.198.05-.371-.025-.52-.075-.149-.669-1.612-.916-2.207-.242-.579-.487-.5-.669-.51-.173-.008-.371-.01-.57-.01-.198 0-.52.074-.792.372-.272.297-1.04 1.016-1.04 2.479 0 1.462 1.065 2.875 1.213 3.074.149.198 2.096 3.2 5.077 4.487.709.306 1.262.489 1.694.625.712.227 1.36.195 1.871.118.571-.085 1.758-.719 2.006-1.413.248-.694.248-1.289.173-1.413-.074-.124-.272-.198-.57-.347m-5.421 7.403h-.004a9.87 9.87 0 01-5.031-1.378l-.361-.214-3.741.982.998-3.648-.235-.374a9.86 9.86 0 01-1.51-5.26c.001-5.45 4.436-9.884 9.888-9.884 2.64 0 5.122 1.03 6.988 2.898a9.825 9.825 0 012.893 6.994c-.003 5.45-4.437 9.884-9.885 9.884m8.413-18.297A11.815 11.815 0 0012.05 0C5.495 0 .16 5.335.157 11.892c0 2.096.547 4.142 1.588 5.945L.057 24l6.305-1.654a11.882 11.882 0 005.683 1.448h.005c6.554 0 11.89-5.335 11.893-11.893a11.821 11.821 0 00-3.48-8.413Z"/>
                </svg>
              </span>
              <span>Contattaci su WhatsApp</span>
            </a>
          </div>
        </div>

      </div>

      <!-- BARRA INFERIORE: COPYRIGHT E LINK LEGALI -->
      <div class="footer-bottom-bar">
        <p class="footer-copyright">
          © <span id="currentYear">2026</span> A.S. TOP CLEAN — Tutti i diritti riservati.
        </p>
        <div class="footer-legal-links">
          <a href="#privacy" class="footer-legal-link">Privacy Policy</a>
          <span class="legal-separator" aria-hidden="true">•</span>
          <a href="#cookies" class="footer-legal-link">Cookie Policy</a>
        </div>
      </div>
    </div>
  </footer>'''

html = html[:idx_main_end] + footer_html + html[idx_main_end:]
html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=9.0', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=9.0', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated with footer successfully!')

# 2. Update css/style.css to append footer styles and responsive rules
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Insert base footer styles right before section 12 responsive design
resp_marker = '/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN GLOBALE'
resp_idx = css.find(resp_marker)

base_footer_css = '''/* ==========================================================================
   12. FOOTER ISTITUZIONALE (.site-footer)
   - Sfondo nero antracite profondo (#04070A) con contrasto tipografico curato
   - Layout in 4 colonne su desktop, fluido su tablet e verticale su mobile
   - Accenti dorati discreti e barra copyright inferiore
   ========================================================================== */

.site-footer {
  position: relative;
  width: 100%;
  background-color: #04070A;
  color: #94A3B8;
  padding: 68px 0 32px 0;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.footer-container {
  width: 100%;
  max-width: var(--container-max-width);
  margin: 0 auto;
  padding: 0 40px;
}

.footer-grid {
  display: grid;
  grid-template-columns: minmax(280px, 1.4fr) minmax(140px, 0.9fr) minmax(180px, 1fr) minmax(240px, 1.2fr);
  gap: 48px 36px;
  padding-bottom: 48px;
}

.footer-col {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

/* Colonna 1: Brand */
.footer-logo-link {
  display: inline-block;
  margin-bottom: 16px;
  transition: opacity var(--transition-fast);
}

.footer-logo-link:hover {
  opacity: 0.85;
}

.footer-logo {
  height: 44px;
  width: auto;
  display: block;
}

.footer-brand-desc {
  font-family: var(--font-primary);
  font-size: 13.5px;
  line-height: 1.62;
  color: #94A3B8;
  margin: 0 0 20px 0;
  max-width: 320px;
}

.footer-social-wrap {
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.footer-social-title {
  font-family: var(--font-primary);
  font-size: 11.5px;
  font-weight: 700;
  letter-spacing: 0.1em;
  color: #CBD5E1;
  text-transform: uppercase;
}

.footer-social-links {
  display: flex;
  align-items: center;
  gap: 10px;
}

.footer-social-btn {
  display: flex;
  align-items: center;
  justify-content: center;
  width: 34px;
  height: 34px;
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: 8px;
  color: #E2E8F0;
  text-decoration: none;
  transition: all var(--transition-fast);
}

.footer-social-btn:hover {
  border-color: var(--color-gold);
  color: var(--color-gold);
  background: rgba(245, 195, 66, 0.08);
  transform: translateY(-2px);
}

/* Intestazioni Colonne */
.footer-heading {
  font-family: var(--font-brand);
  font-size: 15px;
  font-weight: 800;
  letter-spacing: -0.01em;
  color: #FFFFFF;
  margin: 0 0 18px 0;
  position: relative;
  display: inline-block;
}

.footer-heading::after {
  content: '';
  position: absolute;
  bottom: -6px;
  left: 0;
  width: 20px;
  height: 2px;
  background-color: var(--color-gold);
}

/* Liste di Link */
.footer-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.footer-link {
  font-family: var(--font-primary);
  font-size: 13.5px;
  color: #94A3B8;
  text-decoration: none;
  transition: color var(--transition-fast), transform var(--transition-fast);
  display: inline-block;
}

.footer-link:hover {
  color: var(--color-gold);
  transform: translateX(3px);
}

.footer-link:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 2px;
}

/* Colonna Contatti */
.footer-contact-items {
  display: flex;
  flex-direction: column;
  gap: 12px;
  margin-bottom: 20px;
  width: 100%;
}

.footer-contact-item {
  display: flex;
  align-items: center;
  gap: 10px;
  color: #CBD5E1;
  text-decoration: none;
  font-family: var(--font-primary);
  font-size: 13px;
  transition: color var(--transition-fast);
}

.footer-contact-item:hover {
  color: var(--color-gold);
}

.footer-address-item {
  align-items: flex-start;
}

.footer-contact-icon {
  display: flex;
  align-items: center;
  justify-content: center;
  color: var(--color-gold);
  flex-shrink: 0;
  width: 18px;
  height: 18px;
  margin-top: 1px;
}

.footer-cta-wrap {
  width: 100%;
}

.btn-footer-whatsapp {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 10px 18px;
  background-color: var(--color-gold);
  color: #0D151C;
  border-radius: 9999px;
  font-family: var(--font-primary);
  font-size: 13px;
  font-weight: 700;
  text-decoration: none;
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
  box-shadow: 0 2px 10px rgba(245, 195, 66, 0.25);
}

.btn-footer-whatsapp:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
  box-shadow: 0 4px 14px rgba(245, 195, 66, 0.4);
  color: #0D151C;
}

/* Barra Inferiore */
.footer-bottom-bar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-top: 24px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  font-family: var(--font-primary);
  font-size: 12.5px;
  color: #64748B;
  flex-wrap: wrap;
  gap: 12px;
}

.footer-copyright {
  margin: 0;
}

.footer-legal-links {
  display: flex;
  align-items: center;
  gap: 10px;
}

.footer-legal-link {
  color: #64748B;
  text-decoration: none;
  transition: color var(--transition-fast);
}

.footer-legal-link:hover {
  color: var(--color-gold);
}

.legal-separator {
  color: #334155;
  font-size: 10px;
}

'''

css = css[:resp_idx] + base_footer_css + css[resp_idx:]

# Responsive media query additions
# 1. 1280px
css = css.replace(
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }',
    '/* Contatti a 1280px */\n  .contact-container {\n    padding: 0 32px;\n  }\n\n  .contact-layout {\n    grid-template-columns: minmax(240px, 1fr) minmax(340px, 1.35fr) minmax(190px, 0.85fr);\n    gap: 28px;\n  }\n\n  /* Footer a 1280px */\n  .footer-container {\n    padding: 0 32px;\n  }\n\n  .footer-grid {\n    gap: 36px 28px;\n  }'
)

# 2. 1024px
css = css.replace(
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }',
    '/* Contatti su Tablet (1024px) */\n  .contact-section {\n    padding: 56px 0 64px 0;\n  }\n\n  .contact-container {\n    padding: 0 24px;\n  }\n\n  .contact-layout {\n    grid-template-columns: 1fr;\n    gap: 32px;\n  }\n\n  .contact-intro-col {\n    max-width: 650px;\n  }\n\n  .contact-bg-ambient {\n    width: 100%;\n    opacity: 0.16;\n  }\n\n  /* Footer su Tablet (1024px) */\n  .footer-container {\n    padding: 0 24px;\n  }\n\n  .footer-grid {\n    grid-template-columns: repeat(2, 1fr);\n    gap: 36px 28px;\n  }'
)

# 3. 767px
css = css.replace(
    '  .contact-social-icons {\n    display: flex;\n    align-items: center;\n    justify-content: flex-start;\n    gap: 10px;\n  }\n}',
    '  .contact-social-icons {\n    display: flex;\n    align-items: center;\n    justify-content: flex-start;\n    gap: 10px;\n  }\n\n  /* Footer su Mobile (767px) */\n  .site-footer {\n    padding: 48px 0 28px 0;\n  }\n\n  .footer-container {\n    padding: 0 16px;\n  }\n\n  .footer-grid {\n    display: flex;\n    flex-direction: column;\n    gap: 32px;\n    padding-bottom: 32px;\n  }\n\n  .footer-col {\n    width: 100%;\n    align-items: flex-start;\n    text-align: left;\n  }\n\n  .footer-brand-desc {\n    max-width: 100%;\n  }\n\n  .footer-bottom-bar {\n    flex-direction: column;\n    align-items: flex-start;\n    gap: 10px;\n    text-align: left;\n  }\n}'
)

# 4. 480px
css = css.replace(
    '/* Contatti su smartphone compatti (480px) */\n  .contact-section {\n    padding: 40px 0 46px 0;\n  }\n\n  .contact-heading {\n    font-size: 20px;\n  }\n\n  .contact-input {\n    padding: 8.5px 11px;\n    font-size: 12.5px;\n  }',
    '/* Contatti su smartphone compatti (480px) */\n  .contact-section {\n    padding: 40px 0 46px 0;\n  }\n\n  .contact-heading {\n    font-size: 20px;\n  }\n\n  .contact-input {\n    padding: 8.5px 11px;\n    font-size: 12.5px;\n  }\n\n  /* Footer su smartphone compatti (480px) */\n  .footer-heading {\n    font-size: 14.5px;\n  }\n\n  .footer-link {\n    font-size: 13px;\n  }'
)

# 5. 360px
css = css.replace(
    '/* Contatti su smartphone molto piccoli (360px) */\n  .contact-section {\n    padding: 34px 0 40px 0;\n  }\n\n  .contact-container {\n    padding: 0 12px;\n  }\n\n  .contact-heading {\n    font-size: 19px;\n  }\n\n  .btn-contact-whatsapp {\n    font-size: 13px;\n    padding: 10px 16px;\n  }',
    '/* Contatti su smartphone molto piccoli (360px) */\n  .contact-section {\n    padding: 34px 0 40px 0;\n  }\n\n  .contact-container {\n    padding: 0 12px;\n  }\n\n  .contact-heading {\n    font-size: 19px;\n  }\n\n  .btn-contact-whatsapp {\n    font-size: 13px;\n    padding: 10px 16px;\n  }\n\n  /* Footer su smartphone molto piccoli (360px) */\n  .footer-container {\n    padding: 0 12px;\n  }'
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css updated with footer successfully!')

# 3. Update js/main.js to include initFooterYear
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Add to DOMContentLoaded
js = js.replace('initContactWhatsApp();', 'initContactWhatsApp();\n  initFooterYear();')

# Append function
footer_js = '''
/**
 * Aggiorna automaticamente l'anno del copyright nel footer
 */
function initFooterYear() {
  const yearEl = document.getElementById('currentYear');
  if (yearEl) {
    yearEl.textContent = new Date().getFullYear();
  }
}
'''
js += footer_js

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('js/main.js updated with footer successfully!')

