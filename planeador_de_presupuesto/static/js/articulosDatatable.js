let dataTable = document.querySelector('#myTableBody');

var InventoryInfo;

async function getDataTableInfoAsingnaciones() {
    
    let url = 'traslados/getAsignacionesDatatable/'
    // url = 'raw-material/inventoryData/'
    let originalData = true;
    
    
    const req = await callApi(url); // Consumo de Api 
    // const req1 = await callApi('activos/getActivoFijoForm/');



    // validar si la respuesta es ok
    if (req.res.status !== 200) {
        await swalErr('No se obtuvieron datos de inventario, por favor contacte al administrador.');
        return
    }

    // console.log(req1.data)

    console.log(req.data);
    // Aqui se crea el objeto de tabla en JQuery con al que se le entregan los datos para realizar 
    // el rendereo, la busqueda y el ordenamiento de los datos  


        asignacionesTable = $('#myTable').DataTable({
            "data": req.data,
            "pageLength": 25, // Set the number of records per page
            "lengthMenu": [10, 25, 50, 75, 100], // Set the available page lengths
            "columns":[
                {"data": "id"},
                {"data": "sociedad"},
                {"data": "codigo_activo_fijo"},
                {"data": "descripcion"},
                {"data": "usuario_asignado",
                    "render": function ( data,type, row) {
                        if (data != "nan") {
                            return data;
                        }  else {
                            return '';
                        }
                    }
                },
                {"data": "ubicacion"},
                {"data": "fecha_asignacion"},
                {"data": "username"},
                {"data": "acta_de_entrega_firmada",
                "render": function ( data,type, row) {
                    if (data === 1) {
                        return '<span class="equipoAsignado"></span>';
                    }  else {
                        return '<span class="equipoNoAsignado"></span>';
                    }
                }
                },
                {
                    "data": null, // Esta columna no tiene un origen de datos específico                   
                    "defaultContent": "<button id=\"designarEquipo\" alt=\"Esto es del tercer botón\"><i class='bx bx-user-x' ></i></button> <button id=\"generarActa\"><i class='bx bxs-file-export'></i></button>"
                },
                // {
                //     "data": null, // Esta columna no tiene un origen de datos específico
                //     "render": function ( data,type, row) {
                        
                //             return `<td><button class=\"btn btn-secondary BTNactivosAsignados\" id=\"\" onclick=\"abrirVentAux(${row.id_colaborador})\"> <small>Activos Asignados</small> </button></td>`;
                //     }
                //     // "defaultContent": "<td><button class=\"btn btn-secondary BTNactivosAsignados\" id=\"\" onclick=\"abrirVentAux({{ usuario.id_colaborador }})\"> <small>Activos Asignados</small> </button></td>"
                // },

                
                
            ]


        })
    
        return asignacionesTable
}