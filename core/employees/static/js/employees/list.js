$(function () {
    $('#data').DataTable({
        responsive: true,
        autoWidth: false,
        destroy: true,
        deferRender: true,
        ajax: {
            url: window.location.pathname,
            type: 'POST',
            data: {
                'action': 'searchdata'
            },
            dataSrc: ""
        },
        columns: [
            {"data": "id"},
            {"data": "name"},
            {"data": "last_name"},
            {"data": "birthday"},
        ],
        columnDefs: [
            {
                targets: [-1],
                class: 'text-center',
                orderable: false,
                render: function (data, type, row) {
                    let buttons = '<a href="/employees/update/' + row.pk + '/" ' +
                        'class="btn btn-warning btn-xs btn-flat">Editar</a> ';
                    buttons += '<a href="/employees/delete/' + row.pk + '/" type="button" ' +
                        'class="btn btn-danger btn-xs btn-flat">Eliminar</a>';
                    return buttons;
                }
            },
        ],
    });
});