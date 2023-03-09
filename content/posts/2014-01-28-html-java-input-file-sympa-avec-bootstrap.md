---
title: "html/java, input file sympa avec bootstrap"
date: 2014-01-28T13:50:00+01:00
---
Dans le cadre d'un projet, j'ai redesigné un formulaire qui permet d'importer un fichier csv (utilise bootstrap).

Le rendu est le suivant :

<div class="separator" style="clear: both; text-align: center;"><a href="http://2.bp.blogspot.com/-GbpePebl9sw/Uuek_yww54I/AAAAAAAADuw/gMzZw1TdYRA/s1600/Untitled.png" imageanchor="1" style="margin-left: 1em; margin-right: 1em;"><img border="0" src="http://2.bp.blogspot.com/-GbpePebl9sw/Uuek_yww54I/AAAAAAAADuw/gMzZw1TdYRA/s320/Untitled.png" /></a></div>
Le code HTML utilisé est le suivant :


```
     <form method="post" action="/somewhere" enctype="multipart/form-data" class="form-horizontal">
            <div class="control-group">
                <label class="control-label" for="fichier_csv">fichier.csv</label>
                <input type="file" id="fichier_csv" name="fichier_csv" style="display:none" />
                <div class="controls">
                    <div class="input-append">
                        <input id="fichier_path" class="input-large" type="text">
                        <a class="btn" onclick="$('input[id=fichier_csv]').click();">
                            <i class="icon-folder-open"></i>
                            <span>Sélectionner...</span>
                        </a>
                    </div>
                </div>
                <script type="text/javascript">
                    $('input[id=fichier_csv]').change(function() {
                        $('#fichier_path').val($(this).val());
                    });
                </script>
            </div>
	</form>
```

Le code java est le suivant (attention, lorsque le type du formulaire est enctype="multipart/form-data", les paramètres ne se récupèrent plus avec HttpServletRequest.getParameter):


```
   
// récupération des paramètres "autres" que le fichier CSV
if (isMultipartRequest(req)) {
            final DiskFileItemFactory factory = new DiskFileItemFactory();
            final ServletFileUpload upload = new ServletFileUpload(factory);
            upload.setSizeMax(FILE_MAX_SIZE);
            try {
                final List<FileItem> items = upload.parseRequest(req);
                final Iterator<FileItem> it = items.iterator();
                while (it.hasNext()) {
                    final FileItem item = it.next();
                    if (item.isFormField()) {
                        if ("action".equals(item.getFieldName())) {
                            action = item.getString();
                        } else if ("id".equals(item.getFieldName())) {
                            id = item.getString();
                        } else if ("nas".equals(item.getFieldName())) {
                            req.setAttribute("nas", item.getString());
                        }
                    }
                }
                req.setAttribute("fileupload_items", items);
            } catch (final FileUploadException e) {
                LOGGER.error(e);
                throw new RuntimeException(e);
            }
}

...


// récupération du fichier
        List<FileItem> items = (List<FileItem>) req.getAttribute("fileupload_items");
        StringWriter sw_fichier_csv = null;
        for (FileItem item : items) {
            try {
                if(item.isFormField()) {
                    req.setAttribute(item.getFieldName(), item.getString());
                } else {
                    if (item.getFieldName().equals("fichier_csv")) {
                        InputStream fis = item.getInputStream();
                        sw_fichier_csv = new StringWriter();
                        IOUtils.copy(fis, sw_fichier_csv);
                    }
                }
            } catch (IOException e) {
                throw new RuntimeException(e);
            } finally {
                item.delete();
            }
        }
```


