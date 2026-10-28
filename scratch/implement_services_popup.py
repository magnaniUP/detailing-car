import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1.1 Update Main CTA in .services-intro
old_cta = '''            <div class="services-cta-wrapper">
              <a href="#contatti" class="btn-services-all" aria-label="Scopri tutti i servizi di detailing auto e richiedi un preventivo">
                <span>Scopri tutti i servizi</span>
                <svg class="btn-services-arrow" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </a>
            </div>'''

new_cta = '''            <div class="services-cta-wrapper">
              <a href="https://wa.me/393911234567?text=Buongiorno%20A.S.%20Top%20Clean!%20Vorrei%20richiedere%20informazioni%20e%20un%20preventivo%20sui%20vostri%20servizi%20di%20detailing." 
                 class="btn-services-all btn-contact" 
                 id="servicesWhatsAppCta"
                 target="_blank" 
                 rel="noopener noreferrer" 
                 aria-label="Richiedi un preventivo per i servizi di detailing su WhatsApp">
                <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor" width="16" height="16" aria-hidden="true" focusable="false">
                  <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.16 12.04 20.16C10.66 20.16 9.3 19.8 8.11 19.1L7.83 18.93L4.71 19.75L5.54 16.71L5.35 16.41C4.55 15.13 4.13 13.54 4.13 11.91C4.13 7.37 7.82 3.67 12.05 3.67ZM8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.7C7.02 10.92 7.91 12.1 8.03 12.26C8.16 12.43 9.77 14.91 12.23 15.97C12.82 16.22 13.27 16.37 13.63 16.49C14.22 16.67 14.76 16.65 15.19 16.59C15.67 16.51 16.66 15.98 16.87 15.4C17.07 14.81 17.07 14.31 17.01 14.21C16.95 14.11 16.79 14.05 16.54 13.92C16.29 13.8 15.08 13.21 14.85 13.13C14.63 13.04 14.46 13 14.3 13.25C14.13 13.49 13.66 14.05 13.52 14.21C13.38 14.38 13.23 14.4 12.99 14.28C12.74 14.16 11.94 13.9 10.99 13.06C10.25 12.4 9.75 11.59 9.61 11.34C9.46 11.1 9.59 10.96 9.72 10.84C9.83 10.73 9.97 10.55 10.09 10.41C10.22 10.27 10.26 10.16 10.34 10C10.42 9.84 10.38 9.7 10.32 9.58C10.26 9.46 9.77 8.25 9.57 7.76C9.37 7.29 9.17 7.35 9.02 7.34C8.87 7.33 8.71 7.33 8.53 7.33Z"/>
                </svg>
                <span>Richiedi preventivo su WhatsApp</span>
                <svg class="btn-services-arrow" viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                  <line x1="5" y1="12" x2="19" y2="12"></line>
                  <polyline points="12 5 19 12 12 19"></polyline>
                </svg>
              </a>
            </div>'''

if old_cta in html:
    html = html.replace(old_cta, new_cta)
    print('Updated main services CTA to WhatsApp!')
else:
    print('WARNING: old_cta not found in html!')

# 1.2 Update the 6 cards in #servizi: change <a> to <button> with data-service-id
service_mappings = [
    ('Lavaggio Detailing', 'lavaggio-detailing'),
    ('Protezione Ceramica', 'protezione-ceramica'),
    ('Trattamento Interni', 'trattamento-interni'),
    ('Lucidatura e Correzione', 'lucidatura-correzione'),
    ('Restauro Fari', 'restauro-fari'),
    ('Sanificazione Auto', 'sanificazione-auto')
]

for title, s_id in service_mappings:
    # Pattern for link
    pattern = rf'<a href="#contatti" class="service-card-link" aria-label="Scopri di più sul servizio {re.escape(title)}">\s*<span>Scopri di più</span>\s*<svg class="service-link-arrow"[^>]*>.*?</svg>\s*</a>'
    
    replacement = f'''<button type="button" class="service-card-link btn-open-service-modal" data-service-id="{s_id}" aria-haspopup="dialog" aria-label="Scopri i dettagli del servizio {title} e richiedi preventivo su WhatsApp">
                  <span>Scopri di più</span>
                  <svg class="service-link-arrow" viewBox="0 0 24 24" width="13" height="13" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">
                    <line x1="5" y1="12" x2="19" y2="12"></line>
                    <polyline points="12 5 19 12 12 19"></polyline>
                  </svg>
                </button>'''
    
    matches = len(re.findall(pattern, html, flags=re.DOTALL))
    html = re.sub(pattern, replacement, html, count=1, flags=re.DOTALL)
    print(f'Replaced card button for "{title}": {matches > 0}')

# 1.3 Add Modal Dialog HTML right before </body>
modal_html = '''
  <!-- =======================================================================
       POP-UP MODALE: DETTAGLI SERVIZIO & CTA WHATSAPP
       Finestra di dialogo modale accessibile e pienamente responsive (Mobile, Tablet, Notebook)
       ======================================================================= -->
  <div class="service-modal-backdrop" id="serviceModal" aria-hidden="true" role="dialog" aria-modal="true" aria-labelledby="modalServiceTitle">
    <div class="service-modal-dialog" role="document">
      
      <!-- Testata con Immagine del Servizio e Pulsante Chiudi -->
      <div class="service-modal-media-wrap">
        <picture>
          <source id="modalServicePicWebp" srcset="assets/lavaggio-detailing.webp?v=4.0" type="image/webp">
          <img id="modalServiceImg" src="assets/lavaggio-detailing.jpg?v=4.0" alt="" class="service-modal-img" width="800" height="480">
        </picture>
        <div class="service-modal-media-overlay" aria-hidden="true"></div>
        <button type="button" class="service-modal-close" id="closeServiceModalBtn" aria-label="Chiudi finestra dettagli servizio">
          <svg viewBox="0 0 24 24" width="18" height="18" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="18" y1="6" x2="6" y2="18"></line>
            <line x1="6" y1="6" x2="18" y2="18"></line>
          </svg>
        </button>
      </div>

      <!-- Corpo Informativo del Servizio -->
      <div class="service-modal-body">
        <span class="service-modal-eyebrow" id="modalServiceEyebrow">TRATTAMENTO PROFESSIONALE</span>
        <h3 class="service-modal-title" id="modalServiceTitle">Nome Servizio</h3>
        <p class="service-modal-desc" id="modalServiceDesc">Descrizione del servizio...</p>
        
        <div class="service-modal-highlights">
          <h4 class="service-modal-highlights-title">Cosa include questo trattamento:</h4>
          <ul class="service-modal-features-list" id="modalServiceFeatures">
            <!-- Popolato dinamicamente da JavaScript -->
          </ul>
        </div>
      </div>

      <!-- Barra Inferiore con CTA WhatsApp -->
      <div class="service-modal-footer">
        <span class="service-modal-footer-note">Preventivo gratuito e personalizzato in base alla tua auto</span>
        <a href="#" class="btn-modal-whatsapp" id="modalWhatsAppBtn" target="_blank" rel="noopener noreferrer">
          <svg class="icon-whatsapp" viewBox="0 0 24 24" fill="currentColor" width="18" height="18" aria-hidden="true">
            <path d="M12.04 2C6.58 2 2.13 6.45 2.13 11.91C2.13 13.66 2.59 15.36 3.45 16.86L2.05 22L7.3 20.62C8.75 21.41 10.38 21.83 12.04 21.83C17.5 21.83 21.95 17.38 21.95 11.92C21.95 9.27 20.92 6.78 19.05 4.91C17.18 3.03 14.69 2 12.04 2ZM12.05 3.67C14.25 3.67 16.31 4.53 17.87 6.09C19.42 7.65 20.28 9.72 20.28 11.92C20.28 16.46 16.58 20.16 12.04 20.16C10.66 20.16 9.3 19.8 8.11 19.1L7.83 18.93L4.71 19.75L5.54 16.71L5.35 16.41C4.55 15.13 4.13 13.54 4.13 11.91C4.13 7.37 7.82 3.67 12.05 3.67ZM8.53 7.33C8.37 7.33 8.1 7.39 7.87 7.64C7.65 7.89 7.02 8.48 7.02 9.7C7.02 10.92 7.91 12.1 8.03 12.26C8.16 12.43 9.77 14.91 12.23 15.97C12.82 16.22 13.27 16.37 13.63 16.49C14.22 16.67 14.76 16.65 15.19 16.59C15.67 16.51 16.66 15.98 16.87 15.4C17.07 14.81 17.07 14.31 17.01 14.21C16.95 14.11 16.79 14.05 16.54 13.92C16.29 13.8 15.08 13.21 14.85 13.13C14.63 13.04 14.46 13 14.3 13.25C14.13 13.49 13.66 14.05 13.52 14.21C13.38 14.38 13.23 14.4 12.99 14.28C12.74 14.16 11.94 13.9 10.99 13.06C10.25 12.4 9.75 11.59 9.61 11.34C9.46 11.1 9.59 10.96 9.72 10.84C9.83 10.73 9.97 10.55 10.09 10.41C10.22 10.27 10.26 10.16 10.34 10C10.42 9.84 10.38 9.7 10.32 9.58C10.26 9.46 9.77 8.25 9.57 7.76C9.37 7.29 9.17 7.35 9.02 7.34C8.87 7.33 8.71 7.33 8.53 7.33Z"/>
          </svg>
          <span>Richiedi preventivo su WhatsApp</span>
          <svg viewBox="0 0 24 24" width="14" height="14" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <line x1="5" y1="12" x2="19" y2="12"></line>
            <polyline points="12 5 19 12 12 19"></polyline>
          </svg>
        </a>
      </div>

    </div>
  </div>
'''

if 'id="serviceModal"' not in html:
    html = html.replace('</body>', modal_html + '\n</body>')
    print('Added serviceModal HTML before </body>!')

# Bump version to 9.3
html = re.sub(r'css/style\.css\?v=[0-9.]+', 'css/style.css?v=9.3', html)
html = re.sub(r'js/main\.js\?v=[0-9.]+', 'js/main.js?v=9.3', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('index.html updated successfully with services modal & whatsapp cta!')


# 2. Update css/style.css: add modal styles
with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

modal_css = '''
/* ==========================================================================
   13. MODALE DETTAGLI SERVIZIO & LEAD WHATSAPP
   ========================================================================== */

/* Reset pulsante nei card per accessibilità nativa */
button.service-card-link {
  background: none;
  border: none;
  padding: 0;
  margin: 0;
  font: inherit;
  color: inherit;
  cursor: pointer;
  text-align: left;
  display: inline-flex;
  align-items: center;
  gap: 6px;
}

.service-card {
  cursor: pointer;
}

/* Backdrop */
.service-modal-backdrop {
  position: fixed;
  inset: 0;
  z-index: 99999;
  background-color: rgba(4, 7, 10, 0.82);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 20px;
  opacity: 0;
  visibility: hidden;
  transition: opacity 0.28s ease, visibility 0.28s ease;
}

.service-modal-backdrop.is-open {
  opacity: 1;
  visibility: visible;
}

/* Dialog Container */
.service-modal-dialog {
  position: relative;
  width: 100%;
  max-width: 620px;
  max-height: 90vh;
  background: #0D151C;
  border: 1px solid rgba(245, 195, 66, 0.25);
  border-radius: 18px;
  box-shadow: 0 24px 64px rgba(0, 0, 0, 0.75), 0 0 0 1px rgba(255, 255, 255, 0.05);
  display: flex;
  flex-direction: column;
  overflow: hidden;
  transform: scale(0.94) translateY(12px);
  transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
}

.service-modal-backdrop.is-open .service-modal-dialog {
  transform: scale(1) translateY(0);
}

/* Immagine testata */
.service-modal-media-wrap {
  position: relative;
  width: 100%;
  height: 200px;
  overflow: hidden;
  background-color: #070B0E;
  flex-shrink: 0;
}

.service-modal-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
}

.service-modal-media-overlay {
  position: absolute;
  inset: 0;
  background: linear-gradient(180deg, rgba(4, 7, 10, 0.2) 0%, rgba(13, 21, 28, 0.88) 100%);
}

.service-modal-close {
  position: absolute;
  top: 14px;
  right: 14px;
  width: 36px;
  height: 36px;
  border-radius: 50%;
  background: rgba(4, 7, 10, 0.7);
  border: 1px solid rgba(255, 255, 255, 0.2);
  color: #FFFFFF;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast);
  z-index: 2;
}

.service-modal-close:hover {
  background: var(--color-gold);
  color: #0D151C;
  border-color: var(--color-gold);
  transform: rotate(90deg);
}

.service-modal-close:focus-visible {
  outline: 2px solid var(--color-gold);
  outline-offset: 2px;
}

/* Corpo modale */
.service-modal-body {
  padding: 24px 28px 20px 28px;
  overflow-y: auto;
  flex: 1;
}

.service-modal-body::-webkit-scrollbar {
  width: 6px;
}

.service-modal-body::-webkit-scrollbar-track {
  background: rgba(255, 255, 255, 0.04);
}

.service-modal-body::-webkit-scrollbar-thumb {
  background: rgba(245, 195, 66, 0.3);
  border-radius: 3px;
}

.service-modal-eyebrow {
  display: inline-block;
  font-family: var(--font-primary);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.12em;
  color: var(--color-gold);
  text-transform: uppercase;
  margin-bottom: 6px;
}

.service-modal-title {
  font-family: var(--font-brand);
  font-size: 24px;
  font-weight: 800;
  color: #FFFFFF;
  letter-spacing: -0.01em;
  margin: 0 0 12px 0;
}

.service-modal-desc {
  font-family: var(--font-primary);
  font-size: 14px;
  line-height: 1.65;
  color: #CBD5E1;
  margin: 0 0 22px 0;
}

.service-modal-highlights {
  background: rgba(255, 255, 255, 0.03);
  border: 1px solid rgba(255, 255, 255, 0.06);
  border-radius: 12px;
  padding: 16px 18px;
}

.service-modal-highlights-title {
  font-family: var(--font-brand);
  font-size: 12.5px;
  font-weight: 700;
  color: #FFFFFF;
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin: 0 0 12px 0;
}

.service-modal-features-list {
  list-style: none;
  padding: 0;
  margin: 0;
  display: flex;
  flex-direction: column;
  gap: 10px;
}

.service-modal-feature-item {
  display: flex;
  align-items: flex-start;
  gap: 10px;
  font-family: var(--font-primary);
  font-size: 13px;
  line-height: 1.45;
  color: #94A3B8;
}

.service-modal-feature-icon {
  color: var(--color-gold);
  flex-shrink: 0;
  width: 16px;
  height: 16px;
  margin-top: 2px;
}

/* Footer modale con CTA WhatsApp */
.service-modal-footer {
  padding: 18px 28px;
  background-color: #070B0E;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: 16px;
  flex-shrink: 0;
}

.service-modal-footer-note {
  font-family: var(--font-primary);
  font-size: 11.5px;
  color: #64748B;
  max-width: 220px;
  line-height: 1.4;
}

.btn-modal-whatsapp {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 11px 22px;
  background-color: var(--color-gold);
  color: #0D151C;
  border-radius: 9999px;
  font-family: var(--font-primary);
  font-size: 13.5px;
  font-weight: 700;
  text-decoration: none;
  box-shadow: 0 4px 14px rgba(245, 195, 66, 0.35);
  transition: transform var(--transition-fast), box-shadow var(--transition-fast), filter var(--transition-fast);
  white-space: nowrap;
}

.btn-modal-whatsapp:hover {
  transform: translateY(-2px);
  filter: brightness(1.06);
  box-shadow: 0 6px 20px rgba(245, 195, 66, 0.45);
  color: #0D151C;
}

.btn-modal-whatsapp:focus-visible {
  outline: 2px solid #FFFFFF;
  outline-offset: 3px;
}

body.modal-open {
  overflow: hidden !important;
}
'''

# Insert base modal styles before responsive section if not present
if '.service-modal-backdrop' not in css:
    resp_marker = '/* --------------------------------------------------------------------------\n   12. RESPONSIVE DESIGN GLOBALE'
    resp_idx = css.find(resp_marker)
    if resp_idx != -1:
        css = css[:resp_idx] + modal_css + '\n' + css[resp_idx:]
    else:
        css += '\n' + modal_css
    print('Inserted base modal CSS into css/style.css!')

# Add responsive modal styles
# 1. Tablet (1024px)
tablet_modal_css = '''
  /* Modal Servizi su Tablet (1024px) */
  .service-modal-dialog {
    max-width: 560px;
  }
  .service-modal-media-wrap {
    height: 180px;
  }
  .service-modal-body {
    padding: 20px 24px;
  }
  .service-modal-footer {
    padding: 16px 24px;
  }'''

if '/* Modal Servizi su Tablet (1024px) */' not in css:
    # insert before end of 1024px query
    target = '/* Footer su Tablet (1024px) - Layout elegante a 3 livelli centrati */'
    css = css.replace(target, tablet_modal_css + '\n\n  ' + target)
    print('Added tablet modal CSS!')

# 2. Mobile (767px)
mobile_modal_css = '''
  /* Modal Servizi su Mobile (767px) */
  .service-modal-backdrop {
    padding: 12px;
    align-items: flex-end;
  }

  .service-modal-dialog {
    max-width: 100%;
    max-height: 88vh;
    border-radius: 18px 18px 12px 12px;
  }

  .service-modal-media-wrap {
    height: 150px;
  }

  .service-modal-body {
    padding: 16px 16px 14px 16px;
  }

  .service-modal-title {
    font-size: 20px;
  }

  .service-modal-desc {
    font-size: 13px;
    margin-bottom: 16px;
  }

  .service-modal-highlights {
    padding: 12px 14px;
  }

  .service-modal-feature-item {
    font-size: 12.5px;
  }

  .service-modal-footer {
    flex-direction: column;
    align-items: stretch;
    padding: 14px 16px 16px 16px;
    gap: 10px;
  }

  .service-modal-footer-note {
    max-width: 100%;
    text-align: center;
    font-size: 11px;
  }

  .btn-modal-whatsapp {
    width: 100%;
    justify-content: center;
    padding: 11px 18px;
    font-size: 13px;
  }'''

if '/* Modal Servizi su Mobile (767px) */' not in css:
    target = '/* Footer su Mobile (767px) - Layout verticale ordinato conforme al mockup */'
    css = css.replace(target, mobile_modal_css + '\n\n  ' + target)
    print('Added mobile modal CSS!')

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)
print('css/style.css updated successfully with modal styles!')


# 3. Update js/main.js: add initServicesModal and register it
with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

# Make sure COMPANY_CONFIG has the whatsapp phone
if 'whatsappPhone: "",' in js:
    js = js.replace('whatsappPhone: "",', 'whatsappPhone: "393911234567",')
    print('Configured default whatsappPhone to 393911234567!')

# Add initServicesModal to DOMContentLoaded
if 'initServicesModal();' not in js:
    js = js.replace('initServicesSlider();', 'initServicesSlider();\n  initServicesModal();')
    print('Registered initServicesModal in DOMContentLoaded!')

# Add SERVICES_DATA and initServicesModal function
services_js = '''
/**
 * Dati informativi approfonditi per ciascun servizio nel pop-up modale
 */
const SERVICES_DATA = {
  'lavaggio-detailing': {
    eyebrow: "TRATTAMENTO ESTERNO & INTERNO",
    title: "Lavaggio Detailing",
    imageWebp: "assets/lavaggio-detailing.webp?v=4.0",
    imageJpg: "assets/lavaggio-detailing.jpg?v=4.0",
    imageAlt: "Lavaggio detailing professionale auto con schiuma attiva e guanto in microfibra",
    description: "Un lavaggio tecnico e meticoloso che va ben oltre la pulizia convenzionale. Utilizziamo la tecnica a due secchi con griglie protettive antigraffio, shampoo a pH neutro e decontaminazione chimica, per una carrozzeria purificata e protetta da ogni swirl.",
    features: [
      "Prelavaggio schiumogeno (Snow Foam) ad alta densità per rimuovere lo sporco senza attrito",
      "Decontaminazione chimica contro residui ferrosi, catrame, insetti e resine d'albero",
      "Lavaggio manuale a due secchi con guanto in pura microfibra ad alta assorbenza",
      "Detersione approfondita di cerchi in lega, pinze freno, archi ruota e scarichi",
      "Asciugatura a soffio con aria calda filtrata per azzerare il rischio di micro-graffi",
      "Finitura idrofobica rapida e condizionamento nutriente delle guarnizioni esterne"
    ],
    waMessage: "Buongiorno A.S. Top Clean! Vorrei richiedere informazioni e un preventivo per il servizio: Lavaggio Detailing."
  },
  'protezione-ceramica': {
    eyebrow: "NANOTECNOLOGIA & PROTEZIONE VERNICE",
    title: "Protezione Ceramica",
    imageWebp: "assets/protezione-ceramica.webp?v=4.0",
    imageJpg: "assets/protezione-ceramica.jpg?v=4.0",
    imageAlt: "Trattamento di protezione ceramica auto con finitura a specchio e gocce idrofobiche",
    description: "La massima armatura tecnologica per la tua carrozzeria. Applichiamo coating nanoceramici certificati (SiO2) che si legano permanentemente al trasparente dell'auto, creando uno scudo protettivo duraturo, antimacchia e incredibilmente brillante.",
    features: [
      "Preparazione e decontaminazione chimico-meccanica della vernice (Clay Bar)",
      "Applicazione multistrato di coating nanoceramico certificato (durezza 9H)",
      "Effetto idrofobico e autopulente estremo: l'acqua e lo sporco scivolano via all'istante",
      "Scudo impermeabile contro raggi UV, piogge acide, sale stradale ed escrementi d'uccello",
      "Profondità ottica e brillantezza ad effetto specchio che dura anni",
      "Manutenzione e lavaggi futuri notevolmente più rapidi, facili e sicuri"
    ],
    waMessage: "Buongiorno A.S. Top Clean! Vorrei richiedere informazioni e un preventivo per il trattamento: Protezione Ceramica."
  },
  'trattamento-interni': {
    eyebrow: "CURA PELLAME & DETTAGLIO ABITACOLO",
    title: "Trattamento Interni",
    imageWebp: "assets/trattamento-interni.webp?v=4.0",
    imageJpg: "assets/trattamento-interni.jpg?v=4.0",
    imageAlt: "Trattamento interni auto di lusso in pelle nera e finiture in carbonio",
    description: "Rigenerazione e cura sartoriale per ogni elemento dell'abitacolo. Ci prendiamo cura di sedili in pelle, alcantara, tessuti pregiati e plastiche con detergenti specifici a pH bilanciato e lozioni protettive che mantengono la finitura originale opaca e morbida.",
    features: [
      "Detersione e idratazione profonda della pelle con balsami anti-invecchiamento",
      "Lavaggio ad iniezione ed estrazione su moquette, tappetini e vano bagagli",
      "Trattamento delicato per superfici in alcantara con ripristino della naturale morbidezza",
      "Condizionamento antistatico e anti-UV di cruscotto, console e pannelli porta",
      "Pulizia capillare di bocchette di ventilazione, comandi, fessure e guarnizioni",
      "Barriera protettiva invisibile contro macchie accidentali, liquidi e raggi solari"
    ],
    waMessage: "Buongiorno A.S. Top Clean! Vorrei richiedere informazioni e un preventivo per il servizio: Trattamento Interni."
  },
  'lucidatura-correzione': {
    eyebrow: "CORREZIONE DELLA VERNICE (PAINT CORRECTION)",
    title: "Lucidatura e Correzione",
    imageWebp: "assets/lucidatura-correzione.webp?v=4.0",
    imageJpg: "assets/lucidatura-correzione.jpg?v=4.0",
    imageAlt: "Lucidatura professionale carrozzeria auto con lucidatrice rotorbitale",
    description: "Intervento di altissima precisione artigianale dedicato a eliminare difetti visibili della vernice come swirl, ologrammi, opacità e graffi superficiali. Tramite spessimetro digitale e compound nanotecnologici, ripristiniamo la trasparenza e la rifrazione ideale del colore.",
    features: [
      "Ispezione della carrozzeria con lampade da detailing Scangrip ad alto indice di resa cromatica",
      "Misurazione dello spessore del trasparente su ogni pannello con spessimetro digitale",
      "Correzione a più step con lucidatrici rotorbitali e tamponi graduati",
      "Eliminazione fino al 90-95% dei micro-graffi e dei difetti da lavaggi a spazzole",
      "Finitura ultra-fine (Super Finish) per una brillantezza pura senza aloni né ologrammi",
      "Superficie levigata e purificata, ideale per l'applicazione di protettivi nanotecnologici"
    ],
    waMessage: "Buongiorno A.S. Top Clean! Vorrei richiedere informazioni e un preventivo per la Lucidatura e Correzione della carrozzeria."
  },
  'restauro-fari': {
    eyebrow: "SICUREZZA & CHIAREZZA VISIVA",
    title: "Restauro Fari",
    imageWebp: "assets/restauro-fari.webp?v=4.0",
    imageJpg: "assets/restauro-fari.jpg?v=4.0",
    imageAlt: "Restauro fari auto con lenti a LED completamente trasparenti e fascio luminoso nitido",
    description: "Ripristino completo della trasparenza ottica e della sicurezza dei proiettori opacizzati, ingialliti o ossidati dal sole e dal tempo. Non una semplice lucidatura passeggera, ma una levigatura progressiva con applicazione di sigillante protettivo anti-UV a lunga durata.",
    features: [
      "Mascheratura di sicurezza della carrozzeria perimetrale con nastri specifici da detailing",
      "Carteggiatura micrometrica progressiva per eliminare completamente lo strato ossidato",
      "Lucidatura ottica ad alta brillantezza per restituire la totale purezza al policarbonato",
      "Applicazione di sigillante nanotecnologico protettivo UV contro futuri ingiallimenti",
      "Miglioramento immediato dell'efficienza e della profondità del fascio luminoso notturno",
      "Garantisce il pieno rispetto dei parametri di sicurezza e superamento revisione"
    ],
    waMessage: "Buongiorno A.S. Top Clean! Vorrei richiedere informazioni e un preventivo per il servizio: Restauro Fari."
  },
  'sanificazione-auto': {
    eyebrow: "IGIENE CERTIFICATA & VAPORE SECCO",
    title: "Sanificazione Auto",
    imageWebp: "assets/sanificazione-auto.webp?v=4.0",
    imageJpg: "assets/sanificazione-auto.jpg?v=4.0",
    imageAlt: "Trattamento di sanificazione a vapore secco e igienizzazione profonda dell'abitacolo auto",
    description: "Trattamento intensivo di purificazione dell'abitacolo e dei condotti dell'aria condizionata. Neutralizziamo batteri, allergeni, funghi, acari e cattivi odori persistenti (come fumo, umidità o animali), creando un ambiente incontaminato, salubre e sicuro per tutta la famiglia.",
    features: [
      "Sanificazione professionale a vapore secco saturo ad altissima temperatura (180°C)",
      "Disinfezione certificata con presidi medico-chirurgici anallergici e biodegradabili",
      "Bonifica e decontaminazione antibatterica dell'intero impianto di climatizzazione",
      "Neutralizzazione molecolare dei cattivi odori, senza profumi sintetici né residui tossici",
      "Igienizzazione mirata di volante, cambio, cinture, maniglie e sedili bambini",
      "Consigliato per chi soffre di allergie, per la salute dei passeggeri e per auto usate"
    ],
    waMessage: "Buongiorno A.S. Top Clean! Vorrei richiedere informazioni e un preventivo per il servizio: Sanificazione Auto."
  }
};

/**
 * Inizializza il pop-up modale per i dettagli dei servizi e il CTA WhatsApp
 */
function initServicesModal() {
  const modal = document.getElementById('serviceModal');
  if (!modal) return;

  const closeBtn = document.getElementById('closeServiceModalBtn');
  const picWebp = document.getElementById('modalServicePicWebp');
  const imgEl = document.getElementById('modalServiceImg');
  const eyebrowEl = document.getElementById('modalServiceEyebrow');
  const titleEl = document.getElementById('modalServiceTitle');
  const descEl = document.getElementById('modalServiceDesc');
  const featuresListEl = document.getElementById('modalServiceFeatures');
  const waBtn = document.getElementById('modalWhatsAppBtn');

  let lastActiveElement = null;

  function openModal(serviceId) {
    const data = SERVICES_DATA[serviceId];
    if (!data) return;

    lastActiveElement = document.activeElement;

    // Popola i contenuti dinamici
    if (picWebp) picWebp.srcset = data.imageWebp;
    if (imgEl) {
      imgEl.src = data.imageJpg;
      imgEl.alt = data.imageAlt;
    }
    if (eyebrowEl) eyebrowEl.textContent = data.eyebrow;
    if (titleEl) titleEl.textContent = data.title;
    if (descEl) descEl.textContent = data.description;

    // Popola la lista delle caratteristiche
    if (featuresListEl) {
      featuresListEl.innerHTML = '';
      data.features.forEach(feat => {
        const li = document.createElement('li');
        li.className = 'service-modal-feature-item';
        li.innerHTML = `
          <svg class="service-modal-feature-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">
            <polyline points="20 6 9 17 4 12"></polyline>
          </svg>
          <span>${feat}</span>
        `;
        featuresListEl.appendChild(li);
      });
    }

    // Configura il link WhatsApp
    if (waBtn) {
      const phoneClean = (COMPANY_CONFIG.whatsappPhone || '393911234567').replace(/[^0-9]/g, '');
      const encodedMsg = encodeURIComponent(data.waMessage);
      waBtn.href = `https://wa.me/${phoneClean}?text=${encodedMsg}`;
    }

    // Mostra il modal
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');

    // Sposta il focus sul pulsante di chiusura
    setTimeout(() => {
      if (closeBtn) closeBtn.focus();
    }, 50);
  }

  function closeModal() {
    modal.classList.remove('is-open');
    modal.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('modal-open');

    if (lastActiveElement && typeof lastActiveElement.focus === 'function') {
      lastActiveElement.focus();
    }
  }

  // Click su ogni pulsante "Scopri di più" o card
  const serviceCards = document.querySelectorAll('.service-card');
  serviceCards.forEach(card => {
    const btn = card.querySelector('.btn-open-service-modal');
    const serviceId = btn ? btn.getAttribute('data-service-id') : null;

    if (btn && serviceId) {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        e.stopPropagation();
        openModal(serviceId);
      });

      // Opzionale: click sull'intera card apre il modale
      card.addEventListener('click', (e) => {
        // Se non è stato cliccato un link interno diverso
        if (!e.target.closest('a') && !e.target.closest('button')) {
          openModal(serviceId);
        }
      });
    }
  });

  // Handler chiusura
  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  // Chiudi cliccando sul backdrop esterno
  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

  // Chiudi con il tasto Escape e Focus Trap
  window.addEventListener('keydown', (e) => {
    if (!modal.classList.contains('is-open')) return;

    if (e.key === 'Escape' || e.key === 'Esc') {
      e.preventDefault();
      closeModal();
      return;
    }

    if (e.key === 'Tab') {
      const focusable = modal.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (focusable.length === 0) return;

      const firstEl = focusable[0];
      const lastEl = focusable[focusable.length - 1];

      if (e.shiftKey) {
        if (document.activeElement === firstEl) {
          e.preventDefault();
          lastEl.focus();
        }
      } else {
        if (document.activeElement === lastEl) {
          e.preventDefault();
          firstEl.focus();
        }
      }
    }
  });
}
'''

if 'function initServicesModal()' not in js:
    js += services_js
    print('Appended initServicesModal to js/main.js!')

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)
print('js/main.js updated successfully!')

