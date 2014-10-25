define(
    [],
    function() {

  function buildTemplate(tpl) {
    // tpl can either be a precompiled template or the string representing a
    // template... handle both
    if (typeof(tpl) == 'string') {
      tpl = _.template(tpl);
    }   

    function renderWrapper(data) {
      data = data ? data : {}; 
      return tpl(data);
    }   
    return renderWrapper;
  };  

  return {
    buildTemplate : buildTemplate
  }
});
