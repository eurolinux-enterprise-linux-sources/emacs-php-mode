;; Use php-mode for .php,.php3,.php4 and .phtml files

(autoload 'php-mode "php-mode" "Major mode for editing PHP code." t)

(eval-after-load 'php-mode
                 '(require 'php-ext))

(add-to-list 'auto-mode-alist '("\\.php\\(3\\|4\\)?$" . php-mode))
(add-to-list 'auto-mode-alist '("\\.phtml$" . php-mode))
