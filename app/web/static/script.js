document.addEventListener('DOMContentLoaded', () => {
    const select = document.getElementById('shapeSelect');
    const options = {
        polygone: document.getElementById('polygoneOptions'),
        koch: document.getElementById('kochOptions'),
        flower: document.getElementById('flowerOptions')
    };
    function showOptions() {
        Object.values(options).forEach(div => div.style.display = 'none');
        if (options[select.value]) options[select.value].style.display = 'block';
    }
    select.addEventListener('change', showOptions);
    showOptions();


    [
        {checkbox: 'polygoneCheckbox', advanced: 'polygoneAdvanced'},
        {checkbox: 'kochCheckbox', advanced: 'kochAdvanced'},
        {checkbox: 'flowerCheckbox', advanced: 'flowerAdvanced'}
    ].forEach(({checkbox, advanced}) => {
        const cb = document.getElementById(checkbox);
        const adv = document.getElementById(advanced);
        if (cb && adv) {
            const toggle = () => adv.style.display = cb.checked ? 'block' : 'none';
            cb.addEventListener('change', toggle);
            toggle();
        }
    });
});