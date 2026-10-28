/**
 * ============================================================================
 * A.S. TOP CLEAN — DETAILING & CAR CARE
 * Architettura Front-End Vanilla JS: Navigazione, Slider, Accordion e Modulo Preventivo
 * ============================================================================
 */

'use strict';

/**
 * CONFIGURAZIONE AZIENDALE UFFICIALE (WHATSAPP, EMAIL, RECAPITI)
 * Sostituire con i recapiti reali del centro detailing prima della pubblicazione online.
 * Esempio WhatsApp: "393401234567" (prefisso Italia +39 senza + o spazi).
 */
const COMPANY_CONFIG = {
  // Numero WhatsApp ufficiale per ricezione preventivi e contatto rapido
  whatsappPhone: "393911234567",
  // Email ufficiale del centro detailing (opzionale, es. "info@astopclean.it")
  email: "",
  // Numero di telefono fisso o mobile per chiamate vocali (opzionale)
  phone: "",
  // Indirizzo della sede (opzionale, es. "Milano, Italia")
  address: "",
  // Messaggio predefinito per il pulsante contatto rapido
  defaultMessage: "Buongiorno A.S. Top Clean! Vorrei maggiori informazioni sui vostri trattamenti di detailing per la mia auto."
};

/**
 * Retrocompatibilità con i pulsanti WhatsApp dell'Header e del Menu Mobile
 */
const WHATSAPP_CONFIG = {
  get phone() { return COMPANY_CONFIG.whatsappPhone; },
  get message() { return COMPANY_CONFIG.defaultMessage; }
};

document.addEventListener('DOMContentLoaded', () => {
  initMobileMenu();
  initContactButtons();
  initNavLinks();
  initServicesSlider();
  initServicesModal();
  initWorksGallery();
  initWorksModal();
  initFaqAccordion();
  initContactWhatsApp();
  initFooterYear();
});

/**
 * Inizializza il menu di navigazione mobile a tutta larghezza (Full-Width Dropdown)
 * con supporto accessibilità tastiera (ARIA, trap del focus, tasto Esc).
 */
function initMobileMenu() {
  const toggleBtn = document.getElementById('mobileMenuToggle');
  const dropdown = document.getElementById('mobileMenuDropdown');
  const mobileLinks = dropdown ? dropdown.querySelectorAll('a') : [];

  if (!toggleBtn || !dropdown) {
    return;
  }

  let isOpen = false;

  function openMenu() {
    isOpen = true;
    toggleBtn.classList.add('active');
    toggleBtn.setAttribute('aria-expanded', 'true');
    toggleBtn.setAttribute('aria-label', 'Chiudi menu di navigazione');
    dropdown.classList.add('open');
    dropdown.setAttribute('aria-hidden', 'false');
    document.body.classList.add('menu-open');

    // Sposta il focus sul primo elemento focusabile del menu
    const firstFocusable = dropdown.querySelector('a, button');
    if (firstFocusable) {
      setTimeout(() => firstFocusable.focus(), 60);
    }
  }

  function closeMenu() {
    if (!isOpen) return;
    isOpen = false;
    toggleBtn.classList.remove('active');
    toggleBtn.setAttribute('aria-expanded', 'false');
    toggleBtn.setAttribute('aria-label', 'Apri menu di navigazione');
    dropdown.classList.remove('open');
    dropdown.setAttribute('aria-hidden', 'true');
    document.body.classList.remove('menu-open');

    // Ripristina il focus sul pulsante hamburger
    toggleBtn.focus();
  }

  // Toggle al click sul pulsante hamburger/chiudi
  toggleBtn.addEventListener('click', () => {
    if (isOpen) {
      closeMenu();
    } else {
      openMenu();
    }
  });

  // Chiude il menu quando viene cliccato qualsiasi link di navigazione
  mobileLinks.forEach(link => {
    link.addEventListener('click', () => {
      closeMenu();
    });
  });

  // Gestione tastiera (Tasto Escape e Focus Trap)
  window.addEventListener('keydown', (e) => {
    if (!isOpen) return;

    if (e.key === 'Escape' || e.key === 'Esc') {
      e.preventDefault();
      closeMenu();
      return;
    }

    if (e.key === 'Tab') {
      const focusableElements = dropdown.querySelectorAll('button, [href], input, select, textarea, [tabindex]:not([tabindex="-1"])');
      if (focusableElements.length === 0) return;

      const firstEl = focusableElements[0];
      const lastEl = focusableElements[focusableElements.length - 1];

      if (e.shiftKey) {
        // Se Shift + Tab e siamo sul primo elemento, sposta sull'ultimo
        if (document.activeElement === firstEl) {
          e.preventDefault();
          lastEl.focus();
        }
      } else {
        // Se Tab normale e siamo sull'ultimo elemento, torna al primo
        if (document.activeElement === lastEl) {
          e.preventDefault();
          firstEl.focus();
        }
      }
    }
  });

  // Se la finestra viene allargata oltre il breakpoint mobile, chiudi il menu
  window.addEventListener('resize', () => {
    if (window.innerWidth > 980 && isOpen) {
      closeMenu();
    }
  });
}

/**
 * Gestione dei pulsanti di contatto (Header e Menu Mobile)
 */
function initContactButtons() {
  const contactButtons = document.querySelectorAll('.btn-contact');

  contactButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const phoneClean = WHATSAPP_CONFIG.phone.replace(/[^0-9]/g, '');

      if (phoneClean.length >= 8) {
        e.preventDefault();
        const encodedText = encodeURIComponent(WHATSAPP_CONFIG.message);
        const waUrl = `https://wa.me/${phoneClean}?text=${encodedText}`;
        window.open(waUrl, '_blank', 'noopener,noreferrer');
      } else {
        // Se il numero non è ancora impostato, mantiene il link anchor #contatti
      }
    });
  });
}

/**
 * Gestione dello stato attivo delle voci di menu
 */
function initNavLinks() {
  const allNavLinks = document.querySelectorAll('.nav-link, .nav-mobile-link');

  allNavLinks.forEach(link => {
    link.addEventListener('click', function() {
      const targetHref = this.getAttribute('href');

      allNavLinks.forEach(item => {
        if (item.getAttribute('href') === targetHref) {
          item.classList.add('active');
          item.setAttribute('aria-current', 'page');
        } else {
          item.classList.remove('active');
          item.removeAttribute('aria-current');
        }
      });
    });
  });
}

/**
 * Inizializza lo Slider orizzontale touch per le schede dei Servizi su Mobile
 * con snap nativo, navigazione con dots sincronizzati in tempo reale e frecce avanti/indietro.
 */
function initServicesSlider() {
  const grid = document.getElementById('servicesGrid');
  const dotsContainer = document.getElementById('servicesSliderDots');
  const prevBtn = document.getElementById('servicesSliderPrev');
  const nextBtn = document.getElementById('servicesSliderNext');

  if (!grid || !dotsContainer) return;

  const cards = grid.querySelectorAll('.service-card');
  const dots = dotsContainer.querySelectorAll('.slider-dot');

  if (cards.length === 0 || dots.length === 0) return;

  /**
   * Calcola la scheda più vicina al centro visibile del contenitore
   */
  function getCurrentCardIndex() {
    const gridRect = grid.getBoundingClientRect();
    const gridCenter = gridRect.left + gridRect.width / 2;
    let closestIndex = 0;
    let minDistance = Infinity;

    cards.forEach((card, index) => {
      const cardRect = card.getBoundingClientRect();
      const cardCenter = cardRect.left + cardRect.width / 2;
      const distance = Math.abs(cardCenter - gridCenter);
      if (distance < minDistance) {
        minDistance = distance;
        closestIndex = index;
      }
    });

    return closestIndex;
  }

  /**
   * Aggiorna lo stato visivo e ARIA dei dots
   */
  function updateActiveDot(activeIndex) {
    dots.forEach((dot, index) => {
      const isActive = index === activeIndex;
      dot.classList.toggle('active', isActive);
      dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });
  }

  /**
   * Scorre fluidamente alla scheda specificata
   */
  function scrollToCard(index) {
    if (cards[index]) {
      cards[index].scrollIntoView({
        behavior: 'smooth',
        block: 'nearest',
        inline: 'center'
      });
      updateActiveDot(index);
    }
  }

  // Click sui Dots
  dots.forEach((dot, index) => {
    dot.addEventListener('click', () => {
      scrollToCard(index);
    });
  });

  // Click sulla freccia precedente
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      const current = getCurrentCardIndex();
      const prev = Math.max(0, current - 1);
      scrollToCard(prev);
    });
  }

  // Click sulla freccia successiva
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const current = getCurrentCardIndex();
      const next = Math.min(cards.length - 1, current + 1);
      scrollToCard(next);
    });
  }

  // Sincronizzazione in tempo reale durante lo scorrimento touch (debounced con requestAnimationFrame)
  let scrollRaf = null;
  grid.addEventListener('scroll', () => {
    if (scrollRaf) cancelAnimationFrame(scrollRaf);
    scrollRaf = requestAnimationFrame(() => {
      const activeIdx = getCurrentCardIndex();
      updateActiveDot(activeIdx);
    });
  }, { passive: true });
}

/**
 * Inizializza l'interazione della Galleria Fotografica Lavori Eseguiti
 * con supporto scorrimento fluido tramite frecce (< e >), dots indicatori sincronizzati
 * e navigazione touch a scorrimento magnetico.
 */
function initWorksGallery() {
  const grid = document.getElementById('worksGalleryGrid');
  const prevBtn = document.getElementById('worksGalleryPrev');
  const nextBtn = document.getElementById('worksGalleryNext');
  const dotsContainer = document.getElementById('worksGalleryDots');

  if (!grid) return;

  const dots = dotsContainer ? dotsContainer.querySelectorAll('.works-dot') : [];
  const items = grid.querySelectorAll('.works-item');

  if (items.length === 0) return;

  /**
   * Calcola la distanza di scorrimento ideale in base alla larghezza dell'elemento
   */
  function getScrollStep() {
    const firstItem = items[0];
    if (!firstItem) return 200;
    const style = window.getComputedStyle(grid);
    const gap = parseFloat(style.columnGap || style.gap) || 8;
    return (firstItem.offsetWidth + gap) * 2; // Scorre di due colonne alla volta
  }

  /**
   * Aggiorna il dot attivo in base alla percentuale di scorrimento orizzontale
   */
  function updateActiveDot() {
    if (dots.length === 0) return;

    const maxScroll = grid.scrollWidth - grid.clientWidth;
    if (maxScroll <= 0) {
      dots.forEach((dot, idx) => {
        dot.classList.toggle('active', idx === 0);
        dot.setAttribute('aria-selected', idx === 0 ? 'true' : 'false');
      });
      return;
    }

    const progress = grid.scrollLeft / maxScroll;
    const activeIndex = Math.min(dots.length - 1, Math.round(progress * (dots.length - 1)));

    dots.forEach((dot, idx) => {
      const isActive = idx === activeIndex;
      dot.classList.toggle('active', isActive);
      dot.setAttribute('aria-selected', isActive ? 'true' : 'false');
    });
  }

  // Click su Freccia Precedente (<)
  if (prevBtn) {
    prevBtn.addEventListener('click', () => {
      const step = getScrollStep();
      grid.scrollBy({ left: -step, behavior: 'smooth' });
    });
  }

  // Click su Freccia Successiva (>)
  if (nextBtn) {
    nextBtn.addEventListener('click', () => {
      const step = getScrollStep();
      grid.scrollBy({ left: step, behavior: 'smooth' });
    });
  }

  // Click sui Dots inferiori
  dots.forEach((dot, idx) => {
    dot.addEventListener('click', () => {
      const maxScroll = grid.scrollWidth - grid.clientWidth;
      if (maxScroll > 0) {
        const targetScroll = (idx / (dots.length - 1)) * maxScroll;
        grid.scrollTo({ left: targetScroll, behavior: 'smooth' });
      }
    });
  });

  // Sincronizzazione in tempo reale durante lo scorrimento touch / scroll
  let scrollRaf = null;
  grid.addEventListener('scroll', () => {
    if (scrollRaf) cancelAnimationFrame(scrollRaf);
    scrollRaf = requestAnimationFrame(updateActiveDot);
  }, { passive: true });

  // Navigazione da tastiera accessibile con frecce sinistra/destra
  grid.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft') {
      e.preventDefault();
      grid.scrollBy({ left: -getScrollStep(), behavior: 'smooth' });
    } else if (e.key === 'ArrowRight') {
      e.preventDefault();
      grid.scrollBy({ left: getScrollStep(), behavior: 'smooth' });
    }
  });
}

/**
 * Inizializza l'accordion interattivo della sezione FAQ
 * Supporta:
 * - Espansione e chiusura con animazione CSS Grid fluida (0fr -> 1fr)
 * - Aggiornamento dinamico degli attributi ARIA (aria-expanded)
 * - Rotazione a 45 gradi dell'icona "+" dorata all'apertura
 * - Chiusura automatica degli altri elementi aperti per mantenere ordine
 * - Navigazione da tastiera completa conforme WAI-ARIA (Frecce Su/Giù, Home, End)
 */
function initFaqAccordion() {
  const accordion = document.getElementById('faqAccordion') || document.querySelector('.faq-accordion');
  const triggers = accordion 
    ? accordion.querySelectorAll('.faq-trigger') 
    : document.querySelectorAll('.faq-trigger');

  if (triggers.length === 0) return;

  triggers.forEach((trigger, index) => {
    trigger.addEventListener('click', () => {
      const parentItem = trigger.closest('.faq-item');
      if (!parentItem) return;

      const isExpanded = trigger.getAttribute('aria-expanded') === 'true';

      if (isExpanded) {
        // Chiude l'elemento corrente
        parentItem.classList.remove('is-open');
        trigger.setAttribute('aria-expanded', 'false');
      } else {
        // Chiude gli altri elementi aperti per una navigazione ordinata
        const allItems = accordion 
          ? accordion.querySelectorAll('.faq-item') 
          : document.querySelectorAll('.faq-item');

        allItems.forEach(item => {
          if (item !== parentItem) {
            item.classList.remove('is-open');
            const otherTrigger = item.querySelector('.faq-trigger');
            if (otherTrigger) {
              otherTrigger.setAttribute('aria-expanded', 'false');
            }
          }
        });

        // Apre l'elemento corrente
        parentItem.classList.add('is-open');
        trigger.setAttribute('aria-expanded', 'true');
      }
    });

    // Navigazione da tastiera WAI-ARIA
    trigger.addEventListener('keydown', (e) => {
      let targetTrigger = null;

      if (e.key === 'ArrowDown') {
        e.preventDefault();
        targetTrigger = triggers[(index + 1) % triggers.length];
      } else if (e.key === 'ArrowUp') {
        e.preventDefault();
        targetTrigger = triggers[(index - 1 + triggers.length) % triggers.length];
      } else if (e.key === 'Home') {
        e.preventDefault();
        targetTrigger = triggers[0];
      } else if (e.key === 'End') {
        e.preventDefault();
        targetTrigger = triggers[triggers.length - 1];
      }

      if (targetTrigger) {
        targetTrigger.focus();
      }
    });
  });
}

/**
 * Inizializza il collegamento dinamico del pulsante WhatsApp nella sezione Contatti
 */
function initContactWhatsApp() {
  const ctaBtn = document.getElementById('contactWhatsAppCta');
  if (!ctaBtn) return;

  ctaBtn.addEventListener('click', (e) => {
    const phoneClean = COMPANY_CONFIG.whatsappPhone.replace(/[^0-9]/g, '');
    if (phoneClean.length >= 8) {
      e.preventDefault();
      const encodedMsg = encodeURIComponent(COMPANY_CONFIG.defaultMessage);
      const waUrl = `https://wa.me/${phoneClean}?text=${encodedMsg}`;
      window.open(waUrl, '_blank', 'noopener,noreferrer');
    }
  });
}

/**
 * Inizializza l'aggiornamento automatico dell'anno corrente nel footer
 */
function initFooterYear() {
  const currentYearEl = document.getElementById('currentYear');
  if (currentYearEl) {
    currentYearEl.textContent = new Date().getFullYear();
  }
}

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

/**
 * Inizializza il pop-up modale per la galleria di tutti i lavori conclusi
 */
function initWorksModal() {
  const modal = document.getElementById('worksModal');
  const openBtn = document.getElementById('openWorksModalBtn');
  const closeBtn = document.getElementById('closeWorksModalBtn');

  if (!modal || !openBtn) return;

  let lastActiveElement = null;

  function openModal() {
    lastActiveElement = document.activeElement;
    modal.classList.add('is-open');
    modal.setAttribute('aria-hidden', 'false');
    document.body.classList.add('modal-open');

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

  openBtn.addEventListener('click', (e) => {
    e.preventDefault();
    openModal();
  });

  if (closeBtn) {
    closeBtn.addEventListener('click', closeModal);
  }

  modal.addEventListener('click', (e) => {
    if (e.target === modal) {
      closeModal();
    }
  });

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
