"use strict";(self.webpackChunk_N_E=self.webpackChunk_N_E||[]).push([[1536],{61536:function(e,t,r){r.r(t),r.d(t,{default:function(){return h}});var n=r(39977),o=(r(67294),r(44397)),l=r(62541),i=r(55926),u=r(69671),c=r(23408),a=r(45827),s="/_next/static/media/showMore.6c9a6eba.png";function f(e,t,r){return t in e?Object.defineProperty(e,t,{value:r,enumerable:!0,configurable:!0,writable:!0}):e[t]=r,e}function d(e){for(var t=1;t<arguments.length;t++){var r=null!=arguments[t]?arguments[t]:{},n=Object.keys(r);"function"===typeof Object.getOwnPropertySymbols&&(n=n.concat(Object.getOwnPropertySymbols(r).filter((function(e){return Object.getOwnPropertyDescriptor(r,e).enumerable})))),n.forEach((function(t){f(e,t,r[t])}))}return e}function b(e,t){return function(e){if(Array.isArray(e))return e}(e)||function(e,t){var r=[],n=!0,o=!1,l=void 0;try{for(var i,u=e[Symbol.iterator]();!(n=(i=u.next()).done)&&(r.push(i.value),!t||r.length!==t);n=!0);}catch(c){o=!0,l=c}finally{try{n||null==u.return||u.return()}finally{if(o)throw l}}return r}(e,t)||function(){throw new TypeError("Invalid attempt to destructure non-iterable instance")}()}var h=function(e){return(0,n.tZ)(o.td,{id:e.content.id,layout:e.layout,className:"overflow-hidden relative block py-10px px-0",children:(0,n.tZ)("div",{className:"container my-0 mx-auto",children:(0,n.tZ)("div",{className:"max-w-none -mx-2 flex flex-row flex-wrap items-center justify-center",children:e.content.boxes.map((function(e,t){var r=b((0,u.Y)(),2),o=r[0];r[1];return(0,n.BX)(a.f,{box:e.showMore?d({},e,{image:{src:s}}):e,className:"max-lg:w-1/2 w-1/4 relative h-full",children:[(0,n.BX)("div",{className:(0,i.C)(["z-3 absolute text-white text-center py-0 px-10px","sm:bottom-15px left-0 bottom-20px w-full"]),ref:o,children:[e.title&&(0,n.tZ)(l.x,{className:(0,i.C)(["delay-150 w-full mb-5px text-18px","md:delay-15 sm:text-12px font-bold"]),html:e.title}),e.subtitle&&(0,n.tZ)(l.x,{className:(0,i.C)(["delay-50 m-0 w-full text-13px","md:delay-5 sm:text-10px"]),html:e.subtitle})]}),e.icon&&(0,n.tZ)("div",{className:"absolute top-10px left-10px",children:(0,n.tZ)(c.Q,{src:e.icon,height:50,width:50})})]},t)}))})})})}},69671:function(e,t,r){r.d(t,{Y:function(){return l}});var n=r(67294);var o=(e,{root:t,rootMargin:r,threshold:o}={},l=[])=>{const i=(0,n.useRef)(null),u=(0,n.useRef)(null);return(0,n.useCallback)((n=>{i.current&&u.current&&(u.current.unobserve(i.current),u.current.disconnect(),u.current=null),n&&(u.current=new IntersectionObserver(e,{root:t,rootMargin:r,threshold:o}),u.current.observe(n),i.current=n)}),[i,t,r,o,...l])};var l=({root:e,rootMargin:t,threshold:r,unobserveOnEnter:l,target:i,onEnter:u,onLeave:c}={},a=[])=>{const[s,f]=(0,n.useState)({inView:!1,entry:null,observer:null}),d=(0,n.useCallback)((([e],t)=>{const r=t.thresholds.some((t=>e.intersectionRatio>=t))&&e.isIntersecting;f({inView:r,entry:e,observer:t}),r&&l&&(t.unobserve(e.target),t.disconnect()),r?null===u||void 0===u||u(e,t):null===c||void 0===c||c(e,t)}),[u,c,l]),b=o(d,{root:e,rootMargin:t,threshold:r},[l,...a]);return(0,n.useEffect)((()=>{(null===i||void 0===i?void 0:i.current)&&b(i.current)}),[i,b]),[b,s.inView,s.entry,s.observer]}}}]);