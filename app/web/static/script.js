document.addEventListener('DOMContentLoaded', () => {
    [
        {checkbox: 'squareCheckbox', hide: 'squareAdvanced'},
        {checkbox: 'triangleCheckbox', hide: 'triangleAdvanced'},
        {checkbox: 'kochCheckbox', hide: 'kochAdvanced'},
        {checkbox: 'flowerCheckbox', hide: 'flowerAdvanced'}
    ].forEach(({checkbox, hide}) => {
        const checkbox = document.getElementById(checkbox);
        const hide = document.getElementById(hide);
        if (checkbox && hide) {
            const toggle = () => hide.style.display = checkbox.checked ? 'block' : 'none';
            checkbox.addEventListener('change', toggle);
            toggle();
        }
    });
});