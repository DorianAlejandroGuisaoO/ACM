// js/chat.js
(() => {
  // Datos de ejemplo (puedes editarlos)
  const threads = [
    { id: 't1', author: 'Usuario A', text: 'Hola! me interesa el empleo', time: Date.now() - (10*60*1000) },
    { id: 't2', author: 'Usuario B', text: 'Sigue disponible el empleo?', time: Date.now() - (35*60*1000) },
    { id: 't3', author: 'Usuario C', text: 'Contratan recien graduados??', time: Date.now() - (43*60*1000) },
    { id: 't4', author: 'Usuario D', text: 'Donde me postulo!?!?', time: Date.now() - (57*60*1000) },
    { id: 't5', author: 'Usuario E', text: 'Muy buenos días, a donde debo enviar mi solicitud?', time: Date.now() - (60*60*1000) }
  ];

  const threadsEl = document.getElementById('threads');
  const chatWindow = document.getElementById('chatWindow');
  const selectedTitle = document.getElementById('selectedTitle');
  const autoReplyCheckbox = document.getElementById('autoReply');
  const styleInput = document.getElementById('styleInput');
  const replyInput = document.getElementById('replyInput');
  const generateBtn = document.getElementById('generateBtn');
  const sendBtn = document.getElementById('sendBtn');

  let currentThread = null;
  let repliesStore = JSON.parse(localStorage.getItem('acm_replies') || '{}');
  const autoReplied = new Set();

  function timeAgo(ts){
    const diff = Math.floor((Date.now()-ts)/60000); // minutes
    if (diff < 1) return 'Hace un momento';
    if (diff < 60) return `Hace ${diff} minutos`;
    const hours = Math.floor(diff/60);
    return `Hace ${hours} hora${hours>1?'s':''}`;
  }

  function saveStore(){ localStorage.setItem('acm_replies', JSON.stringify(repliesStore)); }

  function renderThreads(){
    threadsEl.innerHTML = '';
    threads.forEach(t=>{
      const div = document.createElement('div');
      div.className = 'thread';
      div.dataset.id = t.id;
      div.innerHTML = `<div class="time">${timeAgo(t.time)}</div><div class="preview">${escapeHtml(t.text)}</div>`;
      div.addEventListener('click', ()=>selectThread(t.id));
      threadsEl.appendChild(div);
    });
  }

  function escapeHtml(s){ return s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }

  function selectThread(id){
    currentThread = threads.find(t=>t.id===id);
    // highlight active
    document.querySelectorAll('.thread').forEach(el=>el.classList.toggle('active', el.dataset.id===id));
    // title
    selectedTitle.textContent = `${currentThread.author} — ${timeAgo(currentThread.time)}`;
    renderChat();
    // auto-reply behavior (generate & send)
    if (autoReplyCheckbox.checked && !autoReplied.has(id)){
      autoReplied.add(id);
      const suggestion = generateReply(currentThread.text, styleInput.value || '');
      pushReply(currentThread.id, suggestion, true);
      renderChat();
    }
  }

  function renderChat(){
    chatWindow.innerHTML = '';
    if (!currentThread){
      chatWindow.innerHTML = `<div class="empty">Selecciona un mensaje para ver el chat y generar una respuesta.</div>`;
      return;
    }
    // incoming original message
    const incomingWrap = document.createElement('div');
    incomingWrap.className = 'msg incoming';
    incomingWrap.innerHTML = `<div class="avatar">${initials(currentThread.author)}</div>
      <div>
        <div class="bubble">${escapeHtml(currentThread.text)}</div>
        <div class="meta">${currentThread.author} · ${timeAgo(currentThread.time)}</div>
      </div>`;
    chatWindow.appendChild(incomingWrap);

    // replies
    const items = (repliesStore[currentThread.id] || []);
    items.forEach(r=>{
      const div = document.createElement('div');
      div.className = 'msg ' + (r.outgoing ? 'outgoing' : 'incoming');
      div.innerHTML = `<div class="avatar">${r.outgoing ? 'AC' : initials(currentThread.author)}</div>
         <div>
           <div class="bubble">${escapeHtml(r.text)}</div>
           <div class="meta">${r.outgoing ? 'Tú' : currentThread.author} · ${timeAgo(r.time)}</div>
         </div>`;
      chatWindow.appendChild(div);
    });

    // scroll bottom
    chatWindow.scrollTop = chatWindow.scrollHeight;
  }

  function initials(name){
    return (name.split(' ').map(p=>p[0]).slice(0,2).join('') || 'U').toUpperCase();
  }

  function pushReply(threadId, text, outgoing=true){
    const entry = { text, time: Date.now(), outgoing: !!outgoing };
    repliesStore[threadId] = repliesStore[threadId] || [];
    repliesStore[threadId].push(entry);
    saveStore();
  }

  // GENERATOR: templates + style application
  function generateReply(original, style){
    const o = (original || '').toLowerCase();
    const templates = [
      {k:'interesa', t:'¡Gracias por tu interés! La vacante está abierta. Puedes aplicar en el enlace de la bio o enviarnos tu CV.'},
      {k:'disponible', t:'Sí, la posición sigue disponible. Envíanos tu hoja de vida o aplica vía el enlace en la bio.'},
      {k:'graduad', t:'Sí, aceptamos recién graduados. Comparte tu CV y lo evaluaremos con gusto.'},
      {k:'postul', t:'Para postularte, completa el formulario en el enlace de la bio o envía tu CV a hr@empresa.com.'},
      {k:'solicitud', t:'Por favor envía tu solicitud y CV al correo indicado o usa el formulario en el enlace.'}
    ];
    let chosen = templates.find(x => o.includes(x.k));
    let base = chosen ? chosen.t : 'Gracias por contactarnos. En breve nuestro equipo te dará toda la información sobre la vacante.';
    const s = (style || '').trim().toLowerCase();

    if (!s) return base;
    if (s.includes('formal')) {
      return `Estimado/a,\n\n${base}\n\nAtentamente,\nEquipo de Reclutamiento`;
    } else if (s.includes('casual')) {
      return `¡Hola! ${base} 😊`;
    } else if (s.includes('breve') || s.includes('corto')) {
      return base.split('. ')[0] + '.';
    } else if (s.includes('entusiasta')) {
      return `${base} ¡Gracias por tu interés! 🎉`;
    } else {
      // si el usuario escribió otra cosa en style, lo agrega como nota
      return `${base}\n\n(Tono solicitado: ${style})`;
    }
  }

  // botones
  generateBtn.addEventListener('click', ()=> {
    if (!currentThread) return alert('Selecciona un mensaje primero.');
    const suggestion = generateReply(currentThread.text, styleInput.value || '');
    replyInput.value = suggestion;
    replyInput.focus();
  });

  sendBtn.addEventListener('click', ()=> {
    if (!currentThread) return alert('Selecciona un mensaje primero.');
    const txt = replyInput.value.trim();
    if (!txt) return;
    pushReply(currentThread.id, txt, true);
    replyInput.value = '';
    renderChat();
  });

  // inicial
  renderThreads();
  renderChat();

})();
