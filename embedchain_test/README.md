# Creating an index

    python process_pdfs.py

I hardwired the directory path for PDF files for my books in the file **process_pdfs.py** - change that for your system.

# Querying the processed PDF files

```
$ python app.py
How can I iterate over a list in Haskell?
To iterate over a list in Haskell, you can use recursion or higher-order functions like `map` or `foldl`. 

How can I edit my Common Lisp files?
To edit Common Lisp files, you can use Emacs with the Lisp editing mode. By setting the default auto-mode-alist in Emacs, whenever you open a file with the extensions ".lisp", ".lsp", or ".cl", Emacs will automatically use the Lisp editing mode. You can search for an "Emacs tutorial" online to learn how to use the basic Emacs editing commands. 

How can I scrape a website using Common Lisp?
One way to scrape a website using Common Lisp is to use the Drakma library. Paul Nathan has written a library using Drakma called web-trotter.lisp, which is available under the AGPL license at articulate-lisp.com/src/web-trotter.lisp. This library can be a good starting point for your scraping project. Additionally, you can use the wget utility to make local copies of a website. The command "wget -m -w 2 http:/knowledgebooks.com/" can be used to mirror a site with a two-second delay between HTTP requests for resources. The option "-m" indicates to recursively follow all links on the website, and the option "-w 2" adds a two-second delay between requests. Another option, "wget -mk -w 2 http:/knowledgebooks.com/", converts URI references to local file references on your local mirror. Concatenating all web pages into one file can also be a useful trick. 
```