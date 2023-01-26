import view
import process
import log


def button_click():
    rezhim = view.inp_mod()
    if rezhim.lower() == 'и':
        sern = view.inp_import()
        res_search = process.search(sern)
        # print(res_search)
        if isinstance(res_search, str):
            view.view_import_no()
        else:
            view.view_import(res_search)
    elif rezhim.lower() == 'э':
        result = view.inp_export()
        process.export(result)

    log.log_view(rezhim)
